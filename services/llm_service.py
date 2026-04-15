import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-lite")
def generate_article(transcript):
    prompt = f"""
    Convert the following YouTube transcript into:

    1. Title
    2. Introduction
    3. Key Insights
    4. Bullet Summary
    5. Conclusion

    Transcript:
    {transcript}
    """

    response = model.generate_content(prompt)
    return response.text