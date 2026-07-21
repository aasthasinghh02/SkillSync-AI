from ai.resume_parser import parse_resume


sample_resume = """
Aastha Singh

Skills:
Python
Java
React
MongoDB

Education:
B.Tech Computer Engineering
"""


result = parse_resume(sample_resume)

print(result)