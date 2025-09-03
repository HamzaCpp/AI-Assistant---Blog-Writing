import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_blog_post(topic: str) -> str:
    prompt = f"Write a short blog post about '{topic}' in 150 words."
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text

def humanize_text(text: str) -> str:
    prompt = f"Rewrite the following text in a more human and friendly tone:\n\n{text}"
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
# utils.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_blog_post(topic: str) -> str:
    prompt = f"Write a short blog post about '{topic}' in 150 words."
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text

def humanize_text(text: str) -> str:
    prompt = f"Rewrite the following text in a more human and friendly tone:\n\n{text}"
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
