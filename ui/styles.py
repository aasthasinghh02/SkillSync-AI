import streamlit as st


def load_css():
    st.markdown(
        """
<style>

/* ==========================================================
   GLOBAL
========================================================== */

html,
body,
[class*="css"]{
    font-family: "Segoe UI", sans-serif;
}


/* Main App */

.main{
    background:#f8fafc;
}


/* Remove Streamlit Branding */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}


/* ==========================================================
   HEADINGS
========================================================== */

h1{

    color:#0f172a;

    font-weight:700;

    letter-spacing:-0.5px;

}

h2{

    color:#1e293b;

    font-weight:600;

}

h3{

    color:#334155;

    font-weight:600;

}


/* ==========================================================
   METRIC CARD
========================================================== */

.metric-card{

    background:white;

    border-radius:18px;

    padding:25px;

    border:1px solid #e2e8f0;

    box-shadow:

        0px 10px 25px rgba(15,23,42,.05);

    transition:.3s;

    margin-bottom:15px;

}


.metric-card:hover{

    transform:translateY(-3px);

}


.metric-title{

    color:#64748b;

    font-size:15px;

    font-weight:600;

}


.metric-value{

    font-size:42px;

    font-weight:700;

    color:#0f172a;

    margin-top:10px;

}


/* ==========================================================
   SECTION CARD
========================================================== */

.section-card{

    background:white;

    border-radius:18px;

    padding:24px;

    border:1px solid #e2e8f0;

    margin-top:18px;

    margin-bottom:18px;

    box-shadow:

        0px 8px 20px rgba(15,23,42,.04);

}


/* ==========================================================
   SUMMARY CARD
========================================================== */

.summary-card{

    background:#eff6ff;

    border-left:6px solid #2563eb;

    border-radius:14px;

    padding:18px;

    color:#1e293b;

    margin-top:10px;

}


/* ==========================================================
   SKILL TAGS
========================================================== */

.skill-tag{

    display:inline-block;

    background:#2563eb;

    color:white;

    padding:

        8px 16px;

    margin:

        6px 6px 6px 0;

    border-radius:30px;

    font-size:14px;

    font-weight:600;

}


/* ==========================================================
   SUCCESS TAG
========================================================== */

.success-tag{

    display:inline-block;

    background:#dcfce7;

    color:#166534;

    padding:10px 18px;

    margin-bottom:8px;

    border-radius:12px;

    width:100%;

}


/* ==========================================================
   WARNING TAG
========================================================== */

.warning-tag{

    display:inline-block;

    background:#fff7ed;

    color:#9a3412;

    padding:10px 18px;

    margin-bottom:8px;

    border-radius:12px;

    width:100%;

}


/* ==========================================================
   ROADMAP CARD
========================================================== */

.roadmap-card{

    background:white;

    border-radius:16px;

    border-left:6px solid #2563eb;

    padding:18px;

    margin-bottom:15px;

    border:1px solid #e2e8f0;

}


/* ==========================================================
   DOWNLOAD BUTTON
========================================================== */

.stDownloadButton button{

    width:100%;

    border-radius:10px;

    font-weight:600;

}


/* ==========================================================
   PRIMARY BUTTON
========================================================== */

.stButton button{

    border-radius:10px;

    font-weight:600;

    height:50px;

}


/* ==========================================================
   FILE UPLOADER
========================================================== */

section[data-testid="stFileUploader"]{

    border-radius:12px;

}


/* ==========================================================
   TEXT AREA
========================================================== */

textarea{

    border-radius:10px !important;

}


/* ==========================================================
   SIDEBAR
========================================================== */

section[data-testid="stSidebar"]{

    background:#ffffff;

    border-right:1px solid #e2e8f0;

}


/* ==========================================================
   DIVIDER
========================================================== */

hr{

    border:0;

    height:1px;

    background:#e2e8f0;

}


/* ==========================================================
   SCROLLBAR
========================================================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#cbd5e1;

    border-radius:10px;

}

::-webkit-scrollbar-thumb:hover{

    background:#94a3b8;

}

</style>
""",
        unsafe_allow_html=True,
    )