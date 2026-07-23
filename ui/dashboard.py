import streamlit as st

from ui.sections import (
    show_ats_analysis,
    show_skill_gap,
    show_learning_roadmap
)


# ==========================================================
# DASHBOARD HEADER
# ==========================================================

def show_header():

    st.title(
        "📊 Resume Intelligence Dashboard"
    )

    st.caption(
        "AI-powered analysis of your resume against the target job description."
    )



# ==========================================================
# RESUME INFORMATION
# ==========================================================

def show_resume_info(
    resume
):

    st.subheader(
        "👤 Resume Profile"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.write(
            "**Name**"
        )

        st.write(
            resume.get(
                "name",
                "Not detected"
            )
        )


        st.write(
            "**Email**"
        )

        st.write(
            resume.get(
                "email",
                "Not detected"
            )
        )


    with col2:

        st.write(
            "**Phone**"
        )

        st.write(
            resume.get(
                "phone",
                "Not detected"
            )
        )


        skills = resume.get(
            "skills",
            []
        )


        st.write(
            f"**Skills Detected:** {len(skills)}"
        )



# ==========================================================
# DASHBOARD CONTROLLER
# ==========================================================

def show_dashboard(
    result
):

    if not result:

        st.info(
            "Upload a resume and run analysis to view results."
        )

        return



    # ------------------------------------------------------
    # Header
    # ------------------------------------------------------

    show_header()


    st.divider()



    # ------------------------------------------------------
    # Resume Information
    # ------------------------------------------------------

    resume = result.get(
        "resume",
        {}
    )


    if resume:

        show_resume_info(
            resume
        )


        st.divider()



    # ------------------------------------------------------
    # ATS ANALYSIS
    # ------------------------------------------------------

    ats = result.get(
        "ats",
        {}
    )


    if ats:

        show_ats_analysis(
            ats
        )


        st.divider()



    # ------------------------------------------------------
    # SKILL GAP
    # ------------------------------------------------------

    skill_gap = result.get(
        "skill_gap",
        {}
    )


    if skill_gap:

        show_skill_gap(
            skill_gap
        )


        st.divider()



    # ------------------------------------------------------
    # LEARNING ROADMAP
    # ------------------------------------------------------

    roadmap = result.get(
        "roadmap",
        {}
    )


    if roadmap:

        show_learning_roadmap(
            roadmap
        )


        st.divider()



    # ------------------------------------------------------
    # Future Modules
    # ------------------------------------------------------

    st.subheader(
        "📥 Reports & Actions"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.button(
            "📄 Generate PDF Report",
            disabled=True,
            use_container_width=True
        )


    with col2:

        st.button(
            "✉️ Generate Cover Letter",
            disabled=True,
            use_container_width=True
        )


    st.caption(
        "More AI-powered features coming soon."
    )