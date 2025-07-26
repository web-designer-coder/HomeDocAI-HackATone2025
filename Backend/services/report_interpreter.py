import os
from dotenv import load_dotenv
import google.generativeai as genai
import fitz  # PyMuPDF for PDF processing

# Load variables from the .env file into the environment
load_dotenv()

# Securely fetch the API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Validate presence
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

# Use the API key to configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")


def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text.strip()


def extract_text_from_image(file_path):
    img = Image.open(file_path)
    return pytesseract.image_to_string(img).strip()


def get_gemini_analysis(text, file_name):
    prompt = f'''
You are a helpful, certified digital medical assistant.
A user has uploaded a medical report named: {file_name}.

Extracted Text:
{text}

Please analyze the report and return a JSON object with the following structure:

1. reportType: (e.g., "Blood Test", "X-ray", "Ultrasound", etc.)
2. keyFindings: (A list of 3–5 brief, patient-friendly bullet points summarizing important medical findings)
3. detailedAnalysis:
    - summary: A short summary of what the report means in simple language for the patient.
    - recommendations: A list of 3–4 easy-to-follow next steps the patient can take. Include lifestyle advice or self-care tips if applicable.
    - riskFactors: A list of any mentioned or inferred medical risk factors (e.g., obesity, smoking, cancer history). Explain each in layman's terms.


**Guidelines:**
- Use simple, non-technical language.
- Highlight if a finding is benign, serious, or needs monitoring.
- Include examples if helpful (e.g., "fatty liver can improve with weight loss and reducing sugar/alcohol intake").
- If breast cancer is mentioned, briefly explain what BIRADS means.

Output JSON only. Do not include extra commentary or markdown. Keep it concise but helpful.
'''
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"
