import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='Digital Skills Lab Python Taught Pre-sessional workshops',
    page_icon="🐍"
)

local_css("css/style.css")

st.title("DSL Python Pre-sessional")


st.markdown(
    """
    **Michael Wiemers**  
    Learning Developer (Data Science Tools)  
    """)

st.image("img/lse_dsl_logo.png", width=400)

st.markdown("---")

cols = st.columns(3)

with cols[1]:
    st.image("img/python_logo.png", width=150)


st.markdown(
    """
    The DSL Python pre-sessional support is divided into two main parts:
    1. The instructions from this website to install Python on your laptop and use Jupyter Notebooks (30 min)
    2. The on-campus pre-sessional workshops to learn the fundamentals of programming in Python (10-12 hours of learning).

    Please follow the instructions on this website to install Python and using Jupyter Notebooks before 
    you join the DSL Python Pre-sessional workshops.
    
    We recommend to set apart 30 minutes to work through this tutorial (excluding the optional sections on installing libraries and managing environments).

    Please work through the pages from the sidebar menu for information about:
    * Why Python is such a popular programming language and why you should learn it.
    * How you can install Python on your personal laptop.
    * The Python Pre-sessional workshops format and timetable.
    * How to access the Python workshop materials on Teams.
    * How to open Jupyter Lab and load a jupyter notebook.
    * How to install libraries and create and manage environments with conda (optional).

    &nbsp;

    <div class="highlight blue">
    If you struggle with any of the steps from this tutorial, we recommend the following:
    <ul>
        <li>Come to the pre-sessional workshops, as detailed in the 
        <a href="https://dsl-python-presessional.streamlit.app/Pre-sessional_Workshops", target="_self">Python Pre-sessional workshops section</a>, 
        to get help and learn Python</li>
        <li>Seek support from our online 1-2-1 or drop-in advice, as detailed on our <a href="https://info.lse.ac.uk/current-students/digital-skills-lab/drop-in-sessions">website</a>.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True
)
