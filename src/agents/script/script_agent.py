from services.gemini_service import GeminiService


class ScriptAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def write_script(self, research_notes):

        prompt = f"""
Use the following research notes to write a YouTube script.

Research Notes:
{research_notes}

The script should include:

- A strong hook
- Introduction
- Main explanation
- Key points
- Conclusion
- Call to action

Make the script simple, engaging, and easy to speak.
"""

        try:
            return self.gemini.generate_content(prompt)

        except Exception as e:
            return f"Script Agent Error: {e}"