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
        
We recommend Anaconda since it simplifies the installation and setup of Python significantly and comes with a set of tools you can
continue to use to an advanced level of proficiency with Python.
            
By installing Anaconda you get:
- **Python**: A recent and stable version of the core Python programming language.
- **VS Code**: One of the best and the most popular tools to write code (not only in Python but most langauges). It has many features that make it a fantastic option for Data Science.
- **Conda**: A package managing tool. With conda you can manage different Python environments and install different versions of Python with ease.
- **Data Science Libraries**: The most popular libraries to work with data are preinstalled.
            
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
### Installing VS Code

1. To install VS Code, go to [this website](https://code.visualstudio.com/download) to download the installer.
    - Windows: select the the x64 option for Intel CPUs and the Arm64 option for ARM CPUs.
    - MacBook: select the Intel Chip version if your MacBook has an Intel CPU and the Apple Silicon if your MacBook has an M1/M2/M3 processor.

        You can find out about the CPU of your MacBook by clicking on the Apple logo in the top-left corner of the screen and then select About this Mac.

""")

st.image("img/vs_code_install.png", width=600)

st.markdown("""

2. Run the installer.
            
                        
### Setting up VS Code
    
1. Open VS Code
    - Windows: Hit the Windows key and type visual studio code. Hit Enter.
    - MacBook: Hit Cmd+Space key and type visual studio code. Hit Enter.

2. In VS Code, on the left-hand menu open the Extensions section.
""")        

st.image("img/vs_code_extensions.png", width=300)

st.markdown(
    """
3. Search for the Python extension and click install.
4. Search for the Jupyter extension and click install.
""")       

st.image("img/vs_code_extensions2.png", width=300)

st.markdown(
    """
### Next step
Go to the Downloading Workshop Materials section and follow the instructions to download the Jupyter Notebooks, which contain the exercises 
 for the Python for Accounting workshops, on your personal laptop.
"""
)
