import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)


def generate_summary(text):

    text = text[:12000]

    prompt = f"""
Summarize the following document into 5 concise bullet points.

Document:

{text}

Summary:
"""

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception:

        # Fallback
        sentences = text.split(".")
        return ". ".join(sentences[:5])