from utils.scoring import calculate_similarity

resume = """
Python
Java
React
MongoDB
Machine Learning
"""

job = """
Python
React
SQL
Machine Learning
"""

score = calculate_similarity(resume, job)

print("Similarity:", score, "%")
