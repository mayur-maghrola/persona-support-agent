import json
from google import genai
from google.genai import types

from src.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def classify_customer_persona(user_message: str) -> dict:
    """
    Classify user into:
    - Technical Expert
    - Frustrated User
    - Business Executive
    """

    system_instruction = """
You are a customer persona classification engine.

Analyze the user's message and classify them into EXACTLY ONE persona:

1. Technical Expert
   - Uses APIs, logs, authentication, configuration, code, debugging terminology

2. Frustrated User
   - Uses emotional language, complaints, urgency, frustration

3. Business Executive
   - Focuses on business impact, timelines, operations, ROI, outcomes

Return ONLY valid JSON.
"""

    response_schema = {
        "type": "OBJECT",
        "properties": {
            "persona": {
                "type": "STRING",
                "enum": [
                    "Technical Expert",
                    "Frustrated User",
                    "Business Executive"
                ]
            },
            "confidence": {
                "type": "NUMBER"
            },
            "reasoning": {
                "type": "STRING"
            }
        },
        "required": [
            "persona",
            "confidence",
            "reasoning"
        ]
    }

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            response_schema=response_schema,
            temperature=0.1
        )
    )

    return json.loads(response.text)