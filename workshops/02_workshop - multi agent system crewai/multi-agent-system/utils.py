import os
import requests
from PyPDF2 import PdfReader
from dotenv import load_dotenv

load_dotenv()

# read resume

def read_resume(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Resume file not found: {file_path}")
    
    if file_path.lower().endswith('.pdf'):
        reader = PdfReader(file_path)
        return " ".join(page.extract_text() or "" for page in reader.pages)
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    

# fetch job descriptions

def fetch_job_description(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text[:5000]
    except requests.RequestException as e:
        return f"Error fetching job description: {e}"