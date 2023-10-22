import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import os
import pycaret

# set App Page
st.title("AUTO-MACHINE LEARNING APP DEVELOPED BY ELVIS DARKO")

# inks to images
auto_url = "https://github.com/elvis-darko/AUTO-MACHINE-LEARNING-WEB-APP-USING-STREAMLIT-AND-PYCARET/raw/main/images/AUTOML.jpg"

with st.sidebar:
    st.image(auto_url, use_column_width=True)
    selected = option_menu(
        menu_title=None,
        options=["Home", "Prediction", "Developers"],
        icons=["house", "droplet", "people"],
        styles=css_style
   )
    