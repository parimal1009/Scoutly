from fastapi import FastAPI, BackgroundTasks, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import shortuuid
from typing import Optional, Union
import io

from utils.database import TalentPipelineDB
from worker import run_sourcing_task
from agents.jd_processor import JDProcessor

app = FastAPI(
    title="Intelligent Sourcing Agent API",
    description="An API to manage and run AI-powered candidate sourcing jobs with JD processing capabilities.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SourcingRequest(BaseModel):
    linkedin_prompt: Optional[str] = Field(None, example="Senior Golang Developer in Bangalore")
    github_prompt: Optional[str] = Field(None, example="Python developer in India with FastAPI contributions")

class JDProcessingRequest(BaseModel):
    job_description_text: str = Field(..., example="We are looking for a Senior Python Developer with 5+ years of experience...")

class JDSourcingRequest(BaseModel):
    job_description_text: Optional[str] = Field(None, example="We are looking for a Senior Python Developer...")
    auto_generate_prompts: bool = Field(True, description="Whether to auto-generate LinkedIn and GitHub prompts from JD")

class JobResponse(BaseModel):
    job_id: str
    status: str
    message: str

class JDProcessingResponse(BaseModel):
    structured_jd: dict
    linkedin_prompt: str
    github_prompt: str
    processing_metadata: dict
    quality_assessment: Optional[dict] = None

db = TalentPipelineDB()
jd_processor = JDProcessor()

@app.post("/sourcing-jobs", status_code=202, response_model=JobResponse)
async def create_sourcing_job(request: SourcingRequest, background_tasks: BackgroundTasks):
    if not request.linkedin_prompt and not request.github_prompt:
        raise HTTPException(status_code=400, detail="At least one prompt (linkedin_prompt or github_prompt) must be provided.")

    job_id = shortuuid.uuid()
    db.create_job(job_id, request.linkedin_prompt, request.github_prompt)
    
    background_tasks.add_task(run_sourcing_task, job_id, request.linkedin_prompt, request.github_prompt)
    
    return {
        "job_id": job_id,
        "status": "pending",
        "message": "Sourcing job has been successfully created and is running in the background."
    }

@app.post("/process-jd", response_model=JDProcessingResponse)
async def process_job_description(request: JDProcessingRequest):
    """
    Process a job description text and generate optimized LinkedIn and GitHub search prompts
    """
    try:
        # Process the job description
        result = jd_processor.process_text_jd(request.job_description_text)
        
        # Validate JD quality
        quality_assessment = jd_processor.validate_jd_quality(result['structured_jd'])
        
        return JDProcessingResponse(
            structured_jd=result['structured_jd'],
            linkedin_prompt=result['linkedin_prompt'],
            github_prompt=result['github_prompt'],
            processing_metadata=result['processing_metadata'],
            quality_assessment=quality_assessment
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing job description: {str(e)}")

@app.post("/process-jd-file")
async def process_job_description_file(
    file: UploadFile = File(...),
    file_type: str = Form(..., description="File type: 'pdf' or 'image'")
):
    """
    Process a job description from uploaded PDF or image file
    """
    try:
        # Validate file type
        if file_type not in ['pdf', 'image']:
            raise HTTPException(status_code=400, detail="file_type must be 'pdf' or 'image'")
        
        # Read file content
        file_content = await file.read()
        
        if len(file_content) == 0:
            raise HTTPException(status_code=400, detail="Uploaded file is empty")
        
        # Process the file
        result = jd_processor.process_job_description(file_content, file_type)
        
        # Validate JD quality
        quality_assessment = jd_processor.validate_jd_quality(result['structured_jd'])
        
        return {
            "structured_jd": result['structured_jd'],
            "linkedin_prompt": result['linkedin_prompt'],
            "github_prompt": result['github_prompt'],
            "processing_metadata": result['processing_metadata'],
            "quality_assessment": quality_assessment,
            "file_info": {
                "filename": file.filename,
                "file_type": file_type,
                "file_size": len(file_content)
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@app.post("/sourcing-jobs-from-jd", status_code=202, response_model=JobResponse)
async def create_sourcing_job_from_jd(request: JDSourcingRequest, background_tasks: BackgroundTasks):
    """
    Create a sourcing job by processing a job description and auto-generating prompts
    """
    try:
        if not request.job_description_text:
            raise HTTPException(status_code=400, detail="job_description_text is required")
        
        job_id = shortuuid.uuid()
        
        if request.auto_generate_prompts:
            # Process JD to generate prompts
            jd_result = jd_processor.process_text_jd(request.job_description_text)
            linkedin_prompt = jd_result['linkedin_prompt']
            github_prompt = jd_result['github_prompt']
            
            # Store additional JD metadata
            db.create_job(job_id, linkedin_prompt, github_prompt, {
                'jd_processed': True,
                'original_jd': request.job_description_text,
                'structured_jd': jd_result['structured_jd'],
                'processing_metadata': jd_result['processing_metadata']
            })
        else:
            # Use the JD text as both prompts (fallback)
            linkedin_prompt = request.job_description_text
            github_prompt = request.job_description_text
            db.create_job(job_id, linkedin_prompt, github_prompt)
        
        background_tasks.add_task(run_sourcing_task, job_id, linkedin_prompt, github_prompt)
        
        return {
            "job_id": job_id,
            "status": "pending",
            "message": f"Sourcing job created from JD processing. LinkedIn: '{linkedin_prompt[:50]}...', GitHub: '{github_prompt[:50]}...'"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating sourcing job from JD: {str(e)}")

@app.post("/sourcing-jobs-from-jd-file", status_code=202)
async def create_sourcing_job_from_jd_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    file_type: str = Form(..., description="File type: 'pdf' or 'image'")
):
    """
    Create a sourcing job by processing a job description file (PDF or image)
    """
    try:
        # Validate file type
        if file_type not in ['pdf', 'image']:
            raise HTTPException(status_code=400, detail="file_type must be 'pdf' or 'image'")
        
        # Read file content
        file_content = await file.read()
        
        if len(file_content) == 0:
            raise HTTPException(status_code=400, detail="Uploaded file is empty")
        
        job_id = shortuuid.uuid()
        
        # Process the file to generate prompts
        jd_result = jd_processor.process_job_description(file_content, file_type)
        linkedin_prompt = jd_result['linkedin_prompt']
        github_prompt = jd_result['github_prompt']
        
        # Store job with JD metadata
        db.create_job(job_id, linkedin_prompt, github_prompt, {
            'jd_processed': True,
            'file_processed': True,
            'filename': file.filename,
            'file_type': file_type,
            'structured_jd': jd_result['structured_jd'],
            'processing_metadata': jd_result['processing_metadata']
        })
        
        background_tasks.add_task(run_sourcing_task, job_id, linkedin_prompt, github_prompt)
        
        return {
            "job_id": job_id,
            "status": "pending",
            "message": f"Sourcing job created from {file_type} file processing. LinkedIn: '{linkedin_prompt[:50]}...', GitHub: '{github_prompt[:50]}...'",
            "file_info": {
                "filename": file.filename,
                "file_type": file_type,
                "file_size": len(file_content)
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating sourcing job from file: {str(e)}")

@app.get("/sourcing-jobs/{job_id}")
async def get_job_status(job_id: str):
    job = db.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@app.get("/sourcing-jobs/{job_id}/results")
async def get_job_results(job_id: str):
    job = db.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if job['status'] != 'completed':
        raise HTTPException(status_code=400, detail=f"Job is not yet complete. Current status: {job['status']}")
        
    results = db.get_candidates_by_job_id(job_id)
    return {
        "job_id": job_id,
        "job_details": job,
        "candidate_count": len(results),
        "candidates": results
    }

@app.get("/sourcing-jobs")
async def list_all_jobs():
    jobs = db.get_all_jobs()
    return {"jobs": jobs}

@app.get("/system-info")
async def get_system_info():
    """
    Get system information about available tools and configurations
    """
    try:
        system_info = jd_processor.jd_parser.get_system_info()
        return {
            "status": "success",
            "system_info": system_info,
            "message": "System configuration retrieved successfully"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "message": "Failed to retrieve system information"
        }

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Intelligent Sourcing Agent API",
        "features": [
            "Traditional sourcing with custom prompts",
            "JD processing from text, PDF, and images",
            "Auto-generated LinkedIn and GitHub search prompts",
            "Multi-agent pipeline for talent sourcing"
        ],
        "endpoints": {
            "process_jd": "/process-jd",
            "process_jd_file": "/process-jd-file", 
            "sourcing_from_jd": "/sourcing-jobs-from-jd",
            "sourcing_from_jd_file": "/sourcing-jobs-from-jd-file",
            "traditional_sourcing": "/sourcing-jobs",
            "system_info": "/system-info"
        }
    }