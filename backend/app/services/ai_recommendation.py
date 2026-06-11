import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a restaurant preference extraction system.

Return ONLY valid JSON.

Schema:
{
  "cuisine": [],
  "budget": "low | medium | high | null",
  "tags": [],
  "location_hint": ""
}

Rules:
- No explanations
- No markdown
- If unknown, use empty values
"""


def extract_preferences(user_input: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=SYSTEM_PROMPT + "\nUser input: " + user_input
    )

    text = response.text.strip()

    try:
        return json.loads(text)
    except Exception:
        return {
            "cuisine": [],
            "budget": None,
            "tags": [],
            "location_hint": ""
        }