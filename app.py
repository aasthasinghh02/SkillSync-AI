import os
import streamlit as st

from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text

from utils.extractor import (
    extract_email,
    extract_phone,
    extract_skills
)

# We will use this in the next step
# from utils.scoring import calculate_similarity

os.makedirs("uploads", exist_ok=True)

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
)

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)


# ----------------------------------------------------
# This entire section runs only AFTER a resume is uploaded
# ----------------------------------------------------
if uploaded_file is not None:

    # Save uploaded file
    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract resume text
    if uploaded_file.name.lower().endswith(".pdf"):
        resume_text = extract_pdf_text(file_path)
    else:
        resume_text = extract_docx_text(file_path)

    st.success("✅ Resume uploaded successfully!")

    # ==========================================
    # NEW SECTION (This is what we are adding)
    # ==========================================

    st.subheader("📄 Job Description")

    job_description = st.text_area(
        "Paste the Job Description below",
        height=200
    )

    # ==========================================
    # NEW BUTTON
    # ==========================================

    if st.button("Analyze Resume"):

        # Extract information
        email = extract_email(resume_text)
        phone = extract_phone(resume_text)
        skills = extract_skills(resume_text)

        # Later we'll calculate similarity
        # similarity = calculate_similarity(
        #     resume_text,
        #     job_description
        # )

        st.subheader("📋 Resume Analysis")

        st.write("### Contact Information")
        st.write("📧 Email:", email)
        st.write("📱 Phone:", phone)

        st.write("### Skills Detected")

        for skill in skills:
            st.write("✅", skill)

        # Later we'll display this
        # st.metric("Match Score", f"{similarity}%")

        st.write("### Resume Text")

        st.text_area(
            "Extracted Resume",
            resume_text,
            height=300
        )

        # ==========================================
        # OpenAI response will go HERE
        # ==========================================

        # ai_result = analyze_resume(
        #     resume_text,
        #     job_description
        # )

        # st.subheader("🤖 AI Feedback")
        # st.markdown(ai_result) 