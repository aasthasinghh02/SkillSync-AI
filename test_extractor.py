from utils.extractor import (
    extract_email,
    extract_phone,
    extract_skills
)


resume_text = """
Aastha Singh
Python Java JavaScript MongoDB
Contact:
+91 7715804704
aasthasinghh08@gmail.com
"""


print("Email:", extract_email(resume_text))

print("Phone:", extract_phone(resume_text))

print("Skills:", extract_skills(resume_text))
