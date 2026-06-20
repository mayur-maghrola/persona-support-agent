from google import genai
from src.config import GEMINI_API_KEY


def generate_response(
    user_query,
    persona,
    context_chunks
):

    client = genai.Client(api_key=GEMINI_API_KEY)

    if persona == "Technical Expert":

        persona_prompt = """
You are a Senior Technical Support Engineer.

Provide:
- Technical explanation
- Root cause analysis
- Step-by-step troubleshooting

Use technical terminology.
"""

    elif persona == "Frustrated User":

        persona_prompt = """
You are an empathetic customer support specialist.

Provide:
- Empathy
- Reassurance
- Simple instructions

Avoid technical jargon.
"""

    else:

        persona_prompt = """
You are a business support manager.

Provide:
- Concise answer
- Business impact
- Resolution timeline

Avoid deep technical details.
"""

    context_text = "\n\n".join(
        [
            f"Source: {c['source']}\n{c['text']}"
            for c in context_chunks
        ]
    )

    prompt = f"""
{persona_prompt}

CONTEXT:
{context_text}

QUESTION:
{user_query}

IMPORTANT:
Answer ONLY from the provided context.
If information is unavailable, say so.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text