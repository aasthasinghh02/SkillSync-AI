from ai.roadmap_generator import generate_roadmap

skills = [
    "FastAPI",
    "Docker",
    "AWS"
]

result = generate_roadmap(skills)

print(result)