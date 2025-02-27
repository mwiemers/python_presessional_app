import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='Digital Skills Lab Python Taught Pre-sessional workshops',
    page_icon="🐍"
)

local_css("css/style.css")

st.title("DSL Python Pre-sessional workshops")


st.markdown(
    """
    **Michael Wiemers**  
    Learning Development Lead (Academic Partnerships)  
    """)

st.image("img/lse_dsl_logo.png", width=400)

st.markdown("---")

cols = st.columns(3)

with cols[1]:
    st.image("img/python_logo.png", width=150)


st.markdown(
    """
    The DSL Python pre-sessional support is divided into two main parts:
    1. The instructions from this website to install Python + VS Code on your laptop to use Jupyter Notebooks (30 min).
    2. The on-campus pre-sessional workshops to learn the fundamentals of programming in Python (10-15 hours of learning).

    Please follow the instructions on this website to install Python + VS Code to use Jupyter Notebooks before 
    you join the DSL Python Pre-sessional workshops.
    
    We recommend to set apart 30 minutes to work through this tutorial (excluding the optional sections on installing libraries and managing environments).

    Please work through the pages from the sidebar menu for information about:
    * Why Python is such a popular programming language and why you should learn it.
    * How you can install Python + VS Code on your personal laptop through Anaconda.
    * The Python Pre-sessional workshops format and timetable.
    * How to access the Python workshop materials from this website.
    * How to access and work with jupyter noteboos in VS Code.

    &nbsp;

    <div class="highlight blue">
    Come to the pre-sessional workshops if you struggle with any of the steps from this tutorial. You can find more information about the workshops in the 
    <a href="https://pypresessionals.streamlit.app/Sign_Up_For_Workshops", target="_self">Python Pre-sessional workshops section</a>.
    </div>
    """, unsafe_allow_html=True
)
