import streamlit as st


# ==========================================================
# METRIC CARD
# ==========================================================

def metric_card(
    title,
    value,
    subtitle=None
):
    """
    Displays KPI cards:
    ATS Score
    Job Match %
    etc.
    """

    subtitle_html = ""

    if subtitle:

        subtitle_html = f"""
        <div style="
            color:#64748b;
            font-size:14px;
            margin-top:8px;
        ">
            {subtitle}
        </div>
        """


    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-title">
                {title}
            </div>


            <div class="metric-value">
                {value}
            </div>


            {subtitle_html}

        </div>
        """,
        unsafe_allow_html=True
    )



# ==========================================================
# SECTION CARD
# ==========================================================

def section_card(
    title,
    content
):
    """
    General purpose information card.
    """

    st.markdown(
        f"""
        <div class="section-card">

            <h3>
                {title}
            </h3>

            <div>
                {content}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )



# ==========================================================
# SUMMARY CARD
# ==========================================================

def summary_card(
    text
):
    """
    Resume summary display.
    """

    st.markdown(
        f"""
        <div class="summary-card">

            {text}

        </div>
        """,
        unsafe_allow_html=True
    )



# ==========================================================
# SKILL BADGE
# ==========================================================

def skill_badge(
    skill
):
    """
    Blue skill chips.
    """

    st.markdown(
        f"""
        <span class="skill-tag">

            {skill}

        </span>
        """,
        unsafe_allow_html=True
    )



# ==========================================================
# SUCCESS ITEM
# ==========================================================

def success_item(
    text
):
    """
    Strength display.
    """

    st.markdown(
        f"""
        <div class="success-tag">

            ✓ {text}

        </div>
        """,
        unsafe_allow_html=True
    )



# ==========================================================
# WARNING ITEM
# ==========================================================

def warning_item(
    text
):
    """
    Weakness display.
    """

    st.markdown(
        f"""
        <div class="warning-tag">

            ⚠ {text}

        </div>
        """,
        unsafe_allow_html=True
    )



# ==========================================================
# ROADMAP CARD
# ==========================================================

def roadmap_card(
    week,
    tasks
):
    """
    Displays weekly learning roadmap.
    """

    task_html = ""

    for task in tasks:

        if isinstance(task, dict):

            task_text = task.get(
                "task",
                ""
            )

        else:

            task_text = task


        task_html += f"""
        <li>
            {task_text}
        </li>
        """


    st.markdown(
        f"""
        <div class="roadmap-card">

            <h3>
                {week}
            </h3>


            <ul>

                {task_html}

            </ul>


        </div>
        """,
        unsafe_allow_html=True
    )



# ==========================================================
# SCORE PROGRESS BAR
# ==========================================================

def score_bar(
    label,
    score
):
    """
    Visual score indicator.
    """

    st.markdown(
        f"""
        <div style="
            margin-top:15px;
            margin-bottom:15px;
        ">

        <b>{label}</b>

        <div style="
            background:#e2e8f0;
            border-radius:20px;
            height:18px;
            margin-top:8px;
        ">


            <div style="
                width:{score}%;
                background:#2563eb;
                height:18px;
                border-radius:20px;
                text-align:right;
                color:white;
                padding-right:8px;
                font-size:12px;
            ">

                {score}%

            </div>


        </div>

        </div>
        """,
        unsafe_allow_html=True
    )