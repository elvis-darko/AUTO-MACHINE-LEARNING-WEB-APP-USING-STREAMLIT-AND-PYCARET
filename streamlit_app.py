import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import pickle
from streamlit_option_menu import option_menu
from streamlit_pandas_profiling import st_profile_report
import os
from pycaret.classification import setup, compare_models, pull, save_model
import warnings
warnings.filterwarnings("ignore")


# set up App page and style
st.title("AUTO-MACHINE LEARNING APP")

css_style = {
    "icon": {"color": "white"},
    "nav-link": {"--hover-color": "grey"},
    "nav-link-selected": {"background-color": "#FF4C1B"},
}

# save dataset to os to be used at anytime
if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=None)


# inks to images
auto_url = "https://github.com/elvis-darko/AUTO-MACHINE-LEARNING-WEB-APP-USING-STREAMLIT-AND-PYCARET/raw/main/images/AUTOML.jpg"


# setup home page of app
def home_page():
    st.image(auto_url, use_column_width=True)


# Set up data upload page
def data_upload_page():
    st.subheader("UPLOAD YOUR DATA FOR MODELING")
    st.info("In this section, users can upload their dataset into the app. Users can also have first hand view of sections of their data, such as the columns")
    data = st.file_uploader("Please, upload your dataset here")
    if data:
        # create a dataframe to read and store data
        df = pd.read_csv(data, index_col=None)
        df.to_csv("sourcedata.csv", index=None)
        st.dataframe(df)


        

# set up profiling page
def data_profiling_page():
    st.subheader("AUTOMATED EXPLORATORY DATA ANALYSIS")
    st.info("In this section, the app performs an automated exploratory analysis on the data. This helps to give users more insight and understanding of their data")
    st.info("NOTE : If no data is uploaded at the Data Upload Page, this page will show an error message.")
    # Data Profile
    report = ProfileReport(df)
    st_profile_report(report)


# Set up Auto Machine Learning
def auto_machine_learning_page():
    st.subheader("AUTOMATED MACHINE LEARNING COMPUTATION")
    st.info("In this section, the app builds and trains different machine learning models with the train data. User has to ONLY identify and enter the target varible")
    st.info("NOTE : If no data is uploaded at the Data Upload Page, this page will show an error message.")
    target = st.selectbox("Please, select your target feature", df.columns)
    if st.button("Train model"):
        setup(df, target = target)
        setup_df = pull()
        st.info("This is the automated machine learning settings")
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.info("This is the Performance of the machine learning models")
        st.dataframe(compare_df)
        best_model

    

# set up downlaod page
def model_download_page():
    st.subheader("DOWNLOAD BEST MODEL")
    st.info("In this section, the app allows users to download and save their best performing models to their local computers")
    st.info("NOTE : If no data is uploaded at the Data Upload Page, this page will show an error message.")
    best_model = compare_models()
    compare_df = pull()
    st.info("This is the Performance of the machine learning models")
    st.dataframe(compare_df)
    best_model
    save_model(best_model, "best_model")
    with open("best_model.pkl", 'rb') as f:
        st.download_button("Please download best model", f, "auto_trained_model.pkl")


# set up developer page
def developers_page():
     st.subheader('THE APP DEVELOPER')
     dev_url = "https://github.com/elvis-darko/Team_Zurich_Capstone_Project/raw/main/Assets/images/developer.png"
     st.image(dev_url, use_column_width=True)
     st.write(f"""
    <p>This Auto-Machine Learning App was dvevloped by Elvis Darko. Elvis Darko is a budding Data Scientist who aspires to be an Artificial Intelligence Engineer. Coming from the commonly non-traditional computer science and mathematics background, Elvis Darko taught himself to code in Python programming language. With a fair leve of coding in python, he joined the Data Science professional training program at Azubi Africa where his skills were honed and was introduced to machine learning. It was from this immensely beneficial program that Elvis came to know about Artificial Intelligence. From there, he has pursued a path of learning and training in the field. In not so long a period to come, elvis will be one of the leading voices and faces of Artificial Intelligence in Africa and the world</p>
    """, unsafe_allow_html=True)


# Set up option menu (side bar)
with st.sidebar:
    st.image(auto_url, use_column_width=True)
    st.info("This applicaton allows a user to build and download an automated machine learning model using streamlit, pandas profiling and pycaret")
    selected = option_menu(
        menu_title=None,
        options=["Home", "Data Upload Page", "Data Profiling Page", "Auto ML Page", "Model Download Page", "Developer Page"],
        icons=["house", "cloud-upload", "clipboard-data", "cpu", "download", "people"],
        styles=css_style
   )
    
if selected == "Home":
    home_page()

elif selected == "Data Upload Page":
    data_upload_page()

elif selected == "Data Profiling Page":
    data_profiling_page()

elif selected == "Auto ML Page":
    auto_machine_learning_page()

elif selected == "Model Download Page":
    model_download_page()

elif selected == "Developer Page":
    developers_page()
