import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

SMALLTALK_SYS = """
You are a helpful and knowledgeable AI assistant.
Answer any type of question clearly and informatively.
"""

def smalltalk_answer(user_text: str) -> str:
    """Gemini se general answer nikalne ke liye"""
    try:
        model = genai.GenerativeModel(MODEL_NAME, system_instruction=SMALLTALK_SYS)
        resp = model.generate_content(user_text)
        return (resp.text or "🤖 Sorry, I couldn’t generate a response.").strip()
    except Exception as e:
        return f"🤖 Error: {str(e)}"