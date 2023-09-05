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
    * On Mac: Open the terminal. You can search for the terminal from the Mac search bar: Hit Cmd+spacebar and type in terminal.
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
### Running Python code in Jupyter Notebooks

Jupyter Notebooks consist of Markdown and code cells. Markdown cells are used to display text, images and other multimedia files, 
whereas code cells are being used to run Python code.

Watch the video below for a walkthrough about Markdown and Code cells and how to run Python code in Jupyter Notebooks.

<div style="position: relative; padding-bottom: 41.25%; height: 0;">
    <iframe src="https://www.loom.com/embed/4a09ba98dd164d1589d2a5e8168f0661?sid=4fed4ed1-f2df-455d-951c-4f55ece99de2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

<div class="timestamps" style="padding-top: 20px">
    <ul style="list-style-type: none; padding-left: 0; color:white">
        <li style="list-style-type: none;"><a href="https://www.loom.com/embed/4a09ba98dd164d1589d2a5e8168f0661?sid=4fed4ed1-f2df-455d-951c-4f55ece99de2&t=00m00s">00:00 Introduction</a></li>
        <li style="list-style-type: none;"><a href="https://www.loom.com/embed/4a09ba98dd164d1589d2a5e8168f0661?sid=4fed4ed1-f2df-455d-951c-4f55ece99de2&t=00m27s">00:27 Navigating to Notebooks Folder</a></li>
        <li style="list-style-type: none;"><a href="https://www.loom.com/embed/4a09ba98dd164d1589d2a5e8168f0661?sid=4fed4ed1-f2df-455d-951c-4f55ece99de2&t=00m51s">00:51 Markdown Cells</a></li>
        <li style="list-style-type: none;"><a href="https://www.loom.com/embed/4a09ba98dd164d1589d2a5e8168f0661?sid=4fed4ed1-f2df-455d-951c-4f55ece99de2&t=01m26s">01:26 Code Cells</a></li>
        <li style="list-style-type: none;"><a href="https://www.loom.com/embed/4a09ba98dd164d1589d2a5e8168f0661?sid=4fed4ed1-f2df-455d-951c-4f55ece99de2&t=02m38s">02:38 Executing Code</a></li>
</div>

""", unsafe_allow_html=True)


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

Go to the <a href="https://dsl-python-presessional.streamlit.app/Pre-sessional_Workshops", target="_self">Pre-sessional workshops section</a> to 
learn about the format of the Python workshops and how to sign up for a session.
""", unsafe_allow_html=True
)
