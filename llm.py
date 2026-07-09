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


def generate_answer(question, context):

    # context is now a list of strings
    context_text = "\n\n".join(context)

    prompt = f"""
You are a document question-answering assistant.

Answer ONLY using the information provided below.

If the answer is not present in the context, say:
"Answer not found in the uploaded document."

Context:
{context_text}

Question:
{question}

Answer:
"""

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        print("GEMINI ERROR:", e)

        if len(context) > 0:
            return (
                "AI service unavailable.\n\n"
                "Most relevant information from the document:\n\n"
                + context[0]
            )

        return "No relevant information found."