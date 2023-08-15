import streamlit as st
from load_css import local_css


st.set_page_config(
    page_title='Opening Jupyter Notebooks',
    page_icon='📙'
)

local_css("css/style.css")

st.title("Opening Jupyter Notebooks")


st.markdown(
    """
### Open jupyter notebooks

If you haven't unzipped and placed the jupyter notebooks in a specific folder, do this first.

To open a jupyter notebook, you will need to launch the jupyter lab app, which you can think of as a web-app running offline from your laptop in the browser.

Follow these steps to open a jupyter notebook in jupyter lab:      
1. Open the terminal/command prompt:
    * On Mac: Open the terminal. You can search for the terminal from the Mac search bar: Hit Cmd+Spacebar and type in terminal.
    * On Windows: Open the command prompt. You can search for the command prompt from the Windows search bar: Hit the Windows key and type in command prompt.
2. In the terminal/command prompt, type and run the following command: jupyter lab. The jupyter lab app will open in your browser.
""")

st.image("img/terminal.png")

st.markdown(
      """
3. In the jupyter lab app, select the folder from the menu on the left side where you keep the jupyter notebooks for the Python workshops.
4. Double-click on the notebook to open it. Your screen should look something like below. Notebooks can be selected from the file explorer on the left side,
        while the notebooks are being displayed in separate tabs on the right. You can change the theme to dark by selecting Settings > Theme > JupyterLab Dark.
        You can use the Cmd+b(Mac) or Ctrl+b(Win) shortcut to show/hide the left sidebar.
""")

st.image("img/jupyter_lab.png")

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
