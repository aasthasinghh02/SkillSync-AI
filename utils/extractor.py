import re


def extract_email(text):
    email_pattern = r'\S+@\S+'
    result = re.findall(email_pattern, text)

    return result[0] if result else None


def extract_phone(text):
    phone_pattern = r'\+?\d[\d\s-]{9,15}'
    result = re.findall(phone_pattern, text)

    return result[0] if result else None


def extract_skills(text):

    skills_list = [
        "Python",
        "Java",
        "JavaScript",
        "React",
        "MongoDB",
        "SQL",
        "HTML",
        "CSS",
        "Machine Learning",
        "AI"
    ]

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
