import streamlit as st
import os
from components import display_cv

# Set page config as the very first Streamlit command
st.set_page_config(page_title="My CV", page_icon="📄", layout="centered")

# Load custom CSS if desired (this must be after set_page_config)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("styles/styles.css")

# Define file paths
cv_text_path = os.path.join("data", "cv_text.txt")
cv_image_path = os.path.join("assets", "cv_image.jpg")

# Display the CV
display_cv(cv_text_path, cv_image_path)
