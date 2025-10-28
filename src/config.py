# src/config.py
from dotenv import load_dotenv
import os

# Load .env file (ensure it exists in project root)
load_dotenv()

# Read keys
OPENAI_API_KEY = os.getenv("OPEN_AI_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Quick validation
if not OPENAI_API_KEY:
    raise ValueError("❌ Missing OPEN_AI_KEY in .env file.")
if not SERPER_API_KEY:
    print("⚠️  Warning: SERPER_API_KEY not set. Web search won't work yet.")

print("✅ Environment variables loaded successfully.")
