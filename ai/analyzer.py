import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an expert ATS (Applicant Tracking System).

Analyze the resume against the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return:

1. ATS Score (0-100)
2. Strengths
3. Weaknesses
4. Missing Skills
5. Resume Improvement Suggestions

Respond in clear markdown.
"""

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt,
    )

    return response.output_text
