import streamlit as st

def load_css():

    st.markdown(
        """
        <style>


        /* =========================
           GLOBAL APP
        ========================= */


        .stApp {

            background:
            linear-gradient(
                135deg,
                #0f172a,
                #111827
            );

        }



        /* =========================
           SIDEBAR
        ========================= */


        [data-testid="stSidebar"] {


            background:
            linear-gradient(
                180deg,
                #020617,
                #111827
            );

        }



        [data-testid="stSidebar"] * {

            color:
            #e5e7eb !important;

        }



        /* Sidebar headings */

        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {

            color:white !important;

        }



        /* =========================
           HEADINGS
        ========================= */


        h1 {

            font-size:
            42px !important;

            font-weight:
            800 !important;

            color:
            #ffffff !important;

        }



        h2 {

            color:
            #f8fafc !important;

        }



        h3 {

            color:
            #e2e8f0 !important;

        }



        p, li {

            color:
            #cbd5e1 !important;

        }



        /* =========================
           CARDS
        ========================= */


        div[data-testid="stVerticalBlock"] > div {

            border-radius:
            16px;

        }



        /* =========================
           INPUT BOXES
        ========================= */


        textarea {

            background:
            #1e293b !important;

            color:white !important;

            border-radius:
            12px !important;

        }



        input {

            background:
            #1e293b !important;

            color:white !important;

        }



        /* =========================
           BUTTON
        ========================= */


        .stButton button {


            background:
            linear-gradient(
                90deg,
                #ff4b4b,
                #ff758c
            );


            color:white;

            font-weight:
            700;


            border-radius:
            12px;


            height:
            50px;

        }



        .stButton button:hover {


            transform:
            scale(1.02);


        }



        </style>

        """,
        unsafe_allow_html=True
    )
