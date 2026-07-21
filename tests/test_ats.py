from ai.ats_analyzer import analyze_ats

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
MongoDB
Git
Docker
REST API
"""

result = analyze_ats(
    resume,
    job_description
)

print(result)