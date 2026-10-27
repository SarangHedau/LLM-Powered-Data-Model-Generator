import json

from google import genai

from config import GOOGLE_API_KEY
from src.prompts import SYSTEM_PROMPT
from src.models import DataModelResponse

client = genai.Client(api_key=GOOGLE_API_KEY)


def generate_data_model(user_prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{SYSTEM_PROMPT}\n\nUser Input:\n{user_prompt}"
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    data = json.loads(text)

    print("=" * 80)
    print("RAW GEMINI RESPONSE")
    print(text)
    print("=" * 80)

    print("=" * 80)
    print("PARSED JSON")
    print(data)
    print("=" * 80)

    validated = DataModelResponse.model_validate(data)

    return validated