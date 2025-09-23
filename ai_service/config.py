import os
from dotenv import load_dotenv
load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN") 
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Make API keys optional for testing - show warnings instead of errors
if not SERPER_API_KEY:
    print("⚠️  WARNING: SERPER_API_KEY not found in .env file. Search functionality may be limited.")

if not GITHUB_ACCESS_TOKEN:
    print("⚠️  WARNING: GITHUB_ACCESS_TOKEN not found in .env file. GitHub scraping functionality may be limited.")

if not GROQ_API_KEY:
    print("⚠️  WARNING: GROQ_API_KEY not found in .env file. LLM processing may fail.")
    print("   Please add GROQ_API_KEY to your .env file for full functionality.")

# Export configuration
config = {
    "SERPER_API_KEY": SERPER_API_KEY,
    "GITHUB_ACCESS_TOKEN": GITHUB_ACCESS_TOKEN,
    "GROQ_API_KEY": GROQ_API_KEY
}