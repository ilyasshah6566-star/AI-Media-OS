Sprint 2 Summary
Goal

Learn the fundamentals required to connect Python with an AI model using professional software engineering practices.

Topics Learned
1. Virtual Environment (.venv)

Purpose:
Create an isolated Python environment for one project.

Why?

Prevent package conflicts
Keep projects independent
Easy recreation on another machine
2. pip

Purpose:
Python's package manager.

Analogy:
Play Store for Python.

Example:

pip install requests
3. Package

Definition:
A collection of reusable Python code that provides additional functionality.

Examples:

requests
python-dotenv
google-genai
4. requirements.txt

Purpose:
Stores every package required for the project.

Benefits:

Easy installation
Easy collaboration
Easy deployment

Command:

pip freeze > requirements.txt
5. .gitignore

Purpose:
Tell Git which files should not be uploaded.

Ignored:

.venv/
.env
pycache/

Reason:

Private or auto-generated files.

6. .env

Purpose:
Store secret information.

Examples:

API Keys
Passwords
Tokens

Reason:

Never expose secrets in source code.

7. Hardcoding

Definition:

Writing sensitive information directly inside code.

Bad Example:

API_KEY = "123456"

Professional Solution:

Store secrets inside .env.

8. python-dotenv

Purpose:

Read variables from the .env file.

Important Functions:

from dotenv import load_dotenv

load_dotenv()
9. API

Definition:

A communication bridge between two software systems.

Analogy:

Restaurant waiter.

10. API Key

Definition:

A unique key used to authenticate your application.

Analogy:

Membership card.

11. Google GenAI SDK

Purpose:

Official Python package used to communicate with Gemini.

Installation:

pip install google-genai
12. Reading Environment Variables

Example:

api_key = os.getenv("GEMINI_API_KEY")

Purpose:

Read secret values from .env.

13. Creating Gemini Client
client = genai.Client(api_key=api_key)

Purpose:

Connect Python with Google's AI service.

14. Sending a Prompt
response = client.models.generate_content(
    model="models/gemini-3.5-flash",
    contents="Explain Artificial Intelligence."
)

Purpose:

Send a request to Gemini.

15. Receiving Response
print(response.text)

Purpose:

Display AI-generated output.

Debugging Lesson

Problem:

404 NOT_FOUND

Reason:

The model name had changed.

Solution:

Use:

client.models.list()

to inspect available models instead of guessing.

Engineering Lessons
Read error messages carefully.
Never expose API keys.
Keep secrets in .env.
Use Git regularly.
Understand code instead of copying it.
Debug by investigating, not guessing.
Milestone

Today AI Media OS successfully communicated with Google Gemini and received its first AI-generated response.