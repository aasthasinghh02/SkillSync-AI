import streamlit as st

from ui.cards import (
    summary_card,
    skill_badge,
    success_item,
    warning_item,
    roadmap_card,
    score_bar,
    section_card
)


# ==========================================================
# SCORE SECTION
# ==========================================================

def show_scores(ats):

    st.subheader("📊 Resume Performance")

    col1, col2 = st.columns(2)


    with col1:

        score_bar(
            "ATS Score",
            ats.get(
                "ats_score",
                0
            )
        )


    with col2:

        score_bar(
            "Job Match",
            ats.get(
                "job_match_percentage",
                0
            )
        )



# ==========================================================
# SUMMARY SECTION
# ==========================================================

def show_summary(
    summary
):

    st.subheader(
        "📝 Resume Summary"
    )


    summary_card(
        summary
    )



# ==========================================================
# STRENGTH SECTION
# ==========================================================

def show_strengths(
    strengths
):

    st.subheader(
        "💪 Strengths"
    )


    if not strengths:

        st.info(
            "No strengths detected."
        )

        return


    for item in strengths:

        success_item(
            item
        )



# ==========================================================
# WEAKNESS SECTION
# ==========================================================

def show_weaknesses(
    weaknesses
):

    st.subheader(
        "⚠️ Areas To Improve"
    )


    if not weaknesses:

        st.success(
            "No major weaknesses detected."
        )

        return


    for item in weaknesses:

        warning_item(
            item
        )



# ==========================================================
# SKILL GAP SECTION
# ==========================================================

def show_skill_gap(
    skill_gap
):

    st.subheader(
        "🎯 Skill Gap Analysis"
    )


    critical = skill_gap.get(
        "critical_skills",
        []
    )


    recommended = skill_gap.get(
        "recommended_skills",
        []
    )


    if critical:

        st.markdown(
            "**Critical Skills Missing**"
        )


        for skill in critical:

            skill_badge(
                skill
            )


    if recommended:

        st.markdown(
            "**Recommended Skills**"
        )


        for skill in recommended:

            skill_badge(
                skill
            )



# ==========================================================
# IMPROVEMENT SECTION
# ==========================================================

def show_improvements(
    suggestions
):

    st.subheader(
        "🚀 Resume Improvement Suggestions"
    )


    if not suggestions:

        st.info(
            "No suggestions available."
        )

        return


    for item in suggestions:

        st.write(
            "✅",
            item
        )



# ==========================================================
# ROADMAP SECTION
# ==========================================================

def show_learning_roadmap(
    roadmap
):

    st.subheader(
        "🛣️ Personalized Learning Roadmap"
    )


    weeks = [
        "week_1",
        "week_2",
        "week_3",
        "week_4"
    ]


    for week in weeks:


        if week not in roadmap:

            continue


        roadmap_card(

            week.replace(
                "_",
                " "
            ).title(),

            roadmap[week]

        )


    if roadmap.get(
        "final_project"
    ):


        st.success(
            "Final Goal: "
            +
            roadmap["final_project"]
        )



# ==========================================================
# FULL ATS SECTION
# ==========================================================

def show_ats_analysis(
    ats
):

    show_scores(
        ats
    )


    st.divider()


    show_summary(
        ats.get(
            "summary",
            ""
        )
    )


    st.divider()


    col1, col2 = st.columns(2)


    with col1:

        show_strengths(
            ats.get(
                "strengths",
                []
            )
        )


    with col2:

        show_weaknesses(
            ats.get(
                "weaknesses",
                []
            )
        )



    st.divider()


    show_improvements(
        ats.get(
            "improvement_suggestions",
            []
        )
    )