from services.gemini_service import GeminiService


class ResearchAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def research(self, topic):

        prompt = f"""
Research the following topic:

{topic}

Provide:

1. Overview
2. Key Facts
3. Opportunities
4. Challenges

Keep the answer simple and structured.
"""

        try:
            return self.gemini.generate_content(prompt)

        except Exception as e:
            return f"Research Agent Error: {e}"