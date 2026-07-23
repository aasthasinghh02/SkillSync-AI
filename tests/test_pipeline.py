from services.analysis_service import analyze_resume_pipeline

resume = """
Python
Java
React
MongoDB

Built MERN applications.
"""

job_description = """
Looking for a Python Developer.

Required Skills:

Python
FastAPI
Docker
Git
MongoDB
REST API
AWS
"""

result = analyze_resume_pipeline(
    resume,
    job_description
)

print(result)