from parser.pdf_parser import extract_pdf_text

resume_text = extract_pdf_text("uploads/resume.pdf")

print(resume_text)
