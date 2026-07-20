from ai.analyzer import analyze_resume

resume = """
Python
React
MongoDB
"""

job = """
Python Developer

Requirements:
Python
React
AWS
Docker
MongoDB
"""

result = analyze_resume(resume, job)

print(result)
