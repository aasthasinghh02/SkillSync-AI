RESUME_PARSER_PROMPT = """
You are an expert resume parser.

Extract the resume into the following JSON schema.

{{
  "name": "",
  "email": "",
  "phone": "",
  "education": [],
  "experience": [],
  "projects": [],
  "skills": [],
  "certifications": []
}}

Rules:

- Return ONLY JSON.
- Do not explain anything.
- Do not use Markdown.
- Do not use ```json.
- Do not add extra text.
- If a field is missing, return an empty string or empty list.

Resume:

{resume}
"""

ATS_ANALYZER_PROMPT = """
You are an expert ATS (Applicant Tracking System).

Compare the resume with the job description.

Return ONLY valid JSON in exactly this format:

{{
    "ats_score": 0,
    "job_match_percentage": 0,
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "summary": "",
    "improvement_suggestions": []
}}

Rules:
- Return ONLY JSON.
- No markdown.
- No explanation.
- No code fences.
- ATS score must be between 0 and 100.
- Job match percentage must be between 0 and 100.

Resume:

{resume}

Job Description:

{job_description}
"""

SKILL_GAP_PROMPT = """
You are an experienced technical recruiter and career mentor.

Compare the resume with the job description.

Return ONLY valid JSON.

{{
    "critical_skills": [],
    "recommended_skills": [],
    "nice_to_have_skills": [],
    "learning_recommendations": [],
    "career_advice": ""
}}

Rules:
- Return ONLY JSON.
- No markdown.
- No explanations.
- Do not use ```.

Resume:

{resume}

Job Description:

{job_description}
"""
ROADMAP_PROMPT = """
You are an expert software engineering mentor.

Create a practical 4-week learning roadmap.

Return ONLY valid JSON.

{{
    "week_1": [],
    "week_2": [],
    "week_3": [],
    "week_4": [],
    "final_project": ""
}}

Rules:
- Return ONLY JSON.
- No markdown.
- No explanations.
- Each week should contain 3–5 practical tasks.

Missing Skills:

{skills}
"""