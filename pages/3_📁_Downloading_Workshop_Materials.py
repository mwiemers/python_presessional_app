import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='Accessing Materials',
    page_icon='📁'
)

local_css("css/style.css")

st.title("Accessing and opening Jupyter Notebooks")

st.markdown("""

    ### Download the Python Pre-sessional workshop materials

    In the Python pre-sessional workshops, we teach Python using Jupyter Notebooks.
    
    You can download the notebooks from below.
    
    ### Python Fundamentals
    
    The Python Fundamentals workshops are for beginners that have no prior experience in programming with Python and cover the following topics:
    - Numerical variables
    - String variables
    - Type casting
    - Lists
    - For loops
    - Conditionals
    - Writing functions
    - Dictionaries
    - While Loops
    - Final Coding Challenges
        
    """)
with open("materials/PF_notebooks.zip", "rb") as f:
    btn = st.download_button(
        label = "Download Python Fundamentals materials",
        data = f,
        file_name = "PF_notebooks.zip",
        mime = "application/zip"
        )


st.markdown(
    """
<br>

<div class="highlight blue">
If you struggle with any of the steps from this tutorial, we recommend the following:
<ul>
    <li>Come to the pre-sessional workshops, as detailed in the Python Pre-sessional workshops section, to get help with the installation and learn Python</li>
    <li>Seek support from our online 1-2-1 or drop-in advice, as detailed on our <a href="https://info.lse.ac.uk/current-students/digital-skills-lab/drop-in-sessions">website</a>.</li>
</ul>
</div>
            
""", unsafe_allow_html=True
)

st.markdown(
    """
### Next step

Go to the Opening Jupyter Notebooks section and follow
the instructions to open the Jupyter Notebooks and Python code in a Jupyter Notebook.
"""
)
