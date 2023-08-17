import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='Accessing Materials',
    page_icon='📁'
)

local_css("css/style.css")

st.title("Accessing and opening Jupyter Notebooks")

st.markdown("""

    ### Access to the DSL-Python-Pre-sessional team on Teams

    The Jupyter Notebooks can be accessed on Teams from the DSL-Python-Pre-sessional team.

    Follow these steps to join the team:

    
    1. Go to the Teams overview in MS Teams, which can be accessed from the sidebar on the left.
    2. Select the Join or create team option on the top right.
    3. Enter the team code **yp5ifrt**.
    4. Click Join Team.
""")

st.image("img/join_team.png")


st.markdown(
    """
### Download the jupyter notebooks

1. Go to the Teams overview in MS Teams, which can be accessed from the sidebar on the left.
2. Select the DSL-Python-Pre-sessional team.
3. Select the Jupyter Notebooks channel.
4. Select the Files tab to access the jupyter notebooks.
5. Click here to toggle selection for all items in the folder.
6. Select the three dot icon to access the Download option.
7. Click Download to download all jupyter notebooks as a zip file.
""")

st.image("img/download_notebooks.png")


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
