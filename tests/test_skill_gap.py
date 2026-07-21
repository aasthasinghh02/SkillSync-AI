from ai.skill_gap import analyze_skill_gap

resume = """
Python
Java
React
MongoDB
"""

job_description = """
Python Developer

Required:

Python
FastAPI
Docker
Git
MongoDB
REST API
AWS
"""

result = analyze_skill_gap(
    resume,
    job_description
)

print(result)