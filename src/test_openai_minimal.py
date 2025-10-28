from openai import OpenAI
import os
from dotenv import load_dotenv

# Explicitly load the .env file from project root
load_dotenv(dotenv_path="../.env")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ Missing OPENAI_API_KEY")
else:
    print("✅ Loaded API key prefix:", api_key[:10])

try:
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say hi in one word"}],
    )
    print("🤖 Response:", response.choices[0].message.content)
except Exception as e:
    import traceback
    traceback.print_exc()
