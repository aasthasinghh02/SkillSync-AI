import os
import streamlit as st

from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text

from services.analysis_service import analyze_resume_pipeline

from ui.dashboard import show_dashboard
from ui.styles import load_css


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="SkillSync AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()


# ==========================================================
# SESSION STATE
# ==========================================================

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "resume_uploaded" not in st.session_state:
    st.session_state.resume_uploaded = False


# ==========================================================
# UPLOAD DIRECTORY
# ==========================================================

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("🚀 SkillSync AI")

    st.markdown("---")

    st.subheader("AI Engine")

    st.success("Llama 3.1 (Ollama)")

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ Resume Parsing")
    st.write("✅ ATS Analysis")
    st.write("✅ Skill Gap Detection")
    st.write("✅ Learning Roadmap")
    st.write("🚧 Cover Letter Generator")
    st.write("🚧 PDF Report")

    st.markdown("---")

    if st.session_state.analysis_result:

        st.success("Resume Analyzed")

    else:

        st.info("Awaiting Analysis")

    st.markdown("---")

    st.caption("Version 2.0")


# ==========================================================
# HEADER
# ==========================================================

st.title("🚀 SkillSync AI")

st.caption("AI-Powered Resume Intelligence Platform")

st.markdown(
"""
Analyze your resume against any job description using AI.

The system provides:

- ATS Score
- Job Match Percentage
- Resume Summary
- Missing Skills
- Improvement Suggestions
- Personalized Learning Roadmap
"""
)

st.divider()


# ==========================================================
# INPUT SECTION
# ==========================================================

left, right = st.columns([1, 2])

with left:

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

with right:

    job_description = st.text_area(
        "Paste Job Description",
        height=220,
        placeholder="Paste the complete Job Description..."
    )


st.write("")

analyze_clicked = st.button(
    "🚀 Analyze Resume",
    type="primary",
    use_container_width=True
)


# ==========================================================
# ANALYSIS
# ==========================================================

if analyze_clicked:

    if uploaded_file is None:

        st.warning("Please upload a resume.")
        st.stop()

    if not job_description.strip():

        st.warning("Please paste a Job Description.")
        st.stop()

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.session_state.resume_uploaded = True

    if uploaded_file.name.lower().endswith(".pdf"):

        resume_text = extract_pdf_text(file_path)

    else:

        resume_text = extract_docx_text(file_path)

    with st.spinner("Analyzing resume..."):

        try:

            result = analyze_resume_pipeline(
                resume_text,
                job_description
            )

            st.session_state.analysis_result = result

            st.success("Analysis completed successfully.")

        except Exception as e:

            st.error("Analysis failed.")

            st.exception(e)


# ==========================================================
# DASHBOARD
# ==========================================================

if st.session_state.analysis_result is not None:

    st.divider()

    show_dashboard(
        st.session_state.analysis_result
    )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "SkillSync AI • Built with Streamlit + Ollama + Local AI"
)