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
## Installing Python with Miniconda
        
With Miniconda you can install Python, Python libraries and easily manage different Python environments on your personal laptop/PC.
""")

st.image("img/conda_logo.svg", caption='Anaconda')


st.markdown(
    """
### Downloading Miniconda Installation File (Win/Mac)
    
Follow the steps from the following video to download the Miniconda installation file for your MacBook or Windows laptop.

#### Mac:
1. Depending on whether your Mac has an M1/M2 or Intel processor, you will have to download a different version of Anaconda. Check the processor 
        type by clicking on the Apple icon in the top left corner of your screen and selecting About this Mac. 
        If you have an M1/M2 processor, you will see Apple M1 in the Overview tab. If you have an Intel processor, you will see Intel in the Overview tab.
""")        

st.image("img/mac_processor.png")

miniconda_download_video = "screen_rec/both/miniconda_download_edited.mp4"  # Replace with your local video file path

play_video(miniconda_download_video)


st.markdown(
    """
### Installing Miniconda (Mac)
    
Follow the steps from the following video to install Miniconda using the installation file for your MacBook.
""")        

miniconda_install_mac_video = "screen_rec/mac/install_miniconda_edited.mp4"  # Replace with your local video file path

play_video(miniconda_install_mac_video)


st.markdown(
    """
### Installing Miniconda (Windows)
    
Follow the steps from the following video to install Miniconda using the installation file for your Windows laptop.
""")        

miniconda_install_win_video = "screen_rec/win/install_miniconda_win_edited.mp4"  # Replace with your local video file path

play_video(miniconda_install_win_video)



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
Go to the Downloading Workshop Materials section and follow the instructions to download the Jupyter Notebooks, which contain the exercises 
 for the Python workshops, on your personal laptop.
"""
)
