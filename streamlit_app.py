import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import os
import pycaret

# set App PageS and style
st.title("AUTO-MACHINE LEARNING APP DEVELOPED BY ELVIS DARKO")

css_style = {
    "icon": {"color": "white"},
    "nav-link": {"--hover-color": "grey"},
    "nav-link-selected": {"background-color": "#FF4C1B"},
}


# inks to images
auto_url = "https://github.com/elvis-darko/AUTO-MACHINE-LEARNING-WEB-APP-USING-STREAMLIT-AND-PYCARET/raw/main/images/AUTOML.jpg"


def home_page():
    st.image(auto_url, use_column_width=True)

def developers_page():
     st.title('THE APP DEVELOPERS')
     dev_url = "https://github.com/elvis-darko/Team_Zurich_Capstone_Project/raw/main/Assets/images/developer.png"
     st.image(dev_url, use_column_width=True)
     st.write(f"""
    <p>This Auto-Machine Learning App was dvevloped by Elvis Darko with guidance from Nicholas Renotte</p>
    """, unsafe_allow_html=True)


# Set up option menu (side bar)
with st.sidebar:
    st.image(auto_url, use_column_width=True)
    selected = option_menu(
        menu_title=None,
        options=["Home", "Prediction", "Developers"],
        icons=["house", "droplet", "people"],
        styles=css_style
   )
    
if selected == "Home":
    home_page()

elif selected == "Prediction":
    prediction_page()

elif selected == "Developers":
    developers_page()