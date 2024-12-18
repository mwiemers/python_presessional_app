import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from load_css import local_css



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
## Installing Anaconda
        
With Anaconda you can install Python, Python libraries and easily manage different Python environments.
            
It has many of the libraries you need for data analysis, data visualisation and machine learning.

It also comes with VS Code, which is a Code Editor, that is easy to use for beginners but still has many features that make it 
a great tool for advanced users.
        
""")

st.image("img/conda_logo.webp", caption='Anaconda', width=500)

st.markdown(
    """
### Installing Anaconda

Depending on whether your Mac has an M1/M2 or Intel processor, you will have to download a different version of miniconda and VS Code. Check the processor 
type by clicking on the Apple icon in the top left corner of your screen and selecting About this Mac. 

If you have an M1/M2 processor, you will see Apple M1 in the Overview tab. If you have an Intel processor, you will see Intel in the Overview tab.

""")        

st.image("img/mac_processor.png", width=400)

st.markdown(
    """
Go to the [Anaconda download website](https://www.anaconda.com/download/success)

Select the downloader for your operating system.

For MacBooks, select the download with the purple outline if you have an M1/M2... processor. Otherwise, select the download with the orange outline.
""")

st.image("img/anaconda_download.png", width=800)

st.markdown(
    """
Run the installer.
""")        



st.markdown(
    """
### Next step
Go to the Downloading Workshop Materials section and follow the instructions to download the Jupyter Notebooks, which contain the exercises 
 for the Python for Accounting workshops, on your personal laptop.
"""
)
