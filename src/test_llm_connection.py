import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# --------------------------------------
# Step 1: Locate and load the .env file
# --------------------------------------
# .env should be in your project root folder (same level as src/)
env_path = Path(__file__).resolve().parents[0].parent / ".env"

print(f"🔍 Current working directory: {os.getcwd()}")
print(f"📂 Script location: {Path(__file__).resolve()}")
print(f"🧭 Trying to load .env from: {env_path}")

# Load environment variables
load_dotenv(dotenv_path=env_path)

# --------------------------------------
# Step 2: Fetch API key from environment
# --------------------------------------
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ Missing OPENAI_API_KEY in .env file")

print("🔑 Loaded API key prefix:", api_key[:10])

# --------------------------------------
# Step 3: Initialize OpenAI client
# --------------------------------------
client = OpenAI(api_key=api_key)

# --------------------------------------
# Step 4: Test a small LLM call
# --------------------------------------
print("🧠 Testing LLM response...")
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # small, fast model for testing
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello and tell me the meaning of RAG in 20 words."},
        ],
    )
    print("✅ LLM Response:\n", response.choices[0].message.content)

except Exception as e:
    print("❌ Error while calling LLM:", e)
