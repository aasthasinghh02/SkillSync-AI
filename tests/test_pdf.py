import os
from parser.pdf_parser import extract_pdf_text

file_path = "uploads/resume.pdf"

print("Current directory:", os.getcwd())
print("File exists:", os.path.exists(file_path))

resume_text = extract_pdf_text(file_path)

print("\n----- Resume Text -----\n")
print(resume_text)
