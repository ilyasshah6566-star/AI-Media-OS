from dotenv import load_dotenv
import os
from google import genai

load_dotenv()


class GeminiService:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate_content(self, prompt):

        response = self.client.models.generate_content(
            model="models/gemini-3.1-flash-lite",
            contents=prompt
        )

        return response.text