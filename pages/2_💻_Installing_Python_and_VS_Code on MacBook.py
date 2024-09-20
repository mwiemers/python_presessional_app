import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from load_css import local_css


def play_video(file_name):
    try:
        with open(file_name, "rb") as file:
            video_bytes = file.read()
        st.video(video_bytes, format="video/mp4", start_time=0)
    except FileNotFoundError:
        st.error(f"Local video file '{file_name}' not found.")

def load_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image


st.set_page_config(
    page_title='Installing Python',
    page_icon="💻"
)

local_css("css/style.css")

st.markdown("""
## Installing Miniconda, Python, Jupyter Notebook and VS Code on your MacBook
        
With Miniconda you can install Python, Python libraries and easily manage different Python environments on your personal laptop.
            
You will use Miniconda in combination with VS Code to write code in Python using Jupyter Notebooks.
            
The final video will show you how to open the Python exercises as jupyter notebooks in VS Code and how to write and run Python code.
""")

st.image("img/conda_logo.webp", caption='Anaconda', width=500)


st.markdown(
    """
### Downloading Miniconda Installation File
    
Follow the steps from the following video to download the Miniconda installation file for your MacBook.

Depending on whether your Mac has an M1/M2 or Intel processor, you will have to download a different version of Anaconda. Check the processor 
type by clicking on the Apple icon in the top left corner of your screen and selecting About this Mac. 
If you have an M1/M2 processor, you will see Apple M1 in the Overview tab. If you have an Intel processor, you will see Intel in the Overview tab.
""")        

st.image("img/mac_processor.png", width=500)

miniconda_download_video = "screen_rec/both/miniconda_download_edited.mp4"  

play_video(miniconda_download_video)


st.markdown(
    """
### Installing Miniconda
    
Follow the steps from the following video to install Miniconda using the installation file for your MacBook.
""")        

miniconda_install_mac_video = "screen_rec/mac/install_miniconda_edited.mp4"  

play_video(miniconda_install_mac_video)


st.markdown(
    """
### Downloading VS Code Installation File
    
Follow the steps from the following video to download the VS Code installation file for your MacBook.
""")        

vs_code_installation_video = "screen_rec/both/download_vs_code_edited.mp4"  

play_video(vs_code_installation_video)



st.markdown(
    """
### Installing and setting up VS Code
    
Follow the steps from the video to install and set up VS Code for Python and Jupyter Notebooks on your MacBook.
""")        

vs_code_installation_mac_video = "screen_rec/mac/install_setup_vs_code_edited.mp4"  

play_video(vs_code_installation_mac_video)



st.markdown(
    """
### Creating a Python environment for Python 3.12 and jupyter notebooks
    
Follow the steps from the following video to set up a Python environment and install all libraries required for Jupyter Notebooks.

An environment in programming is like a folder on your computer with a specific version of a programming language, i.e. Python 3.12, and the libraries you need 
to work with the programming language. We use environments so that we can work with different versions of Python. At this point, to work with the Python exercises,
you will only need this one environment with Python 3.12 and the jupyter notebook libraries.

""")        

create_python_env_video = "screen_rec/both/create_python_env_edited.mp4" 

play_video(create_python_env_video)






st.markdown(
    """
<br>

 <div class="highlight blue">
    Come to the pre-sessional workshops if you struggle with any of the steps from this tutorial. You can find more information about the workshops in the 
    <a href="https://dsl-python-presessional.streamlit.app/Pre-sessional_Workshops", target="_self">Python Pre-sessional workshops section</a>.
    </div>
    """, unsafe_allow_html=True
)

st.markdown(
    """
### Next step
Go to the Downloading Workshop Materials section and follow the instructions to download the Jupyter Notebooks, which contain the exercises 
 for the Python workshops, on your personal laptop.
"""
)
