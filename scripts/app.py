import streamlit as st
import os
from components import display_cv

# Set page config
st.set_page_config(page_title="My CV", page_icon="📄", layout="centered")

# Define file paths
cv_text_path = os.path.join("data", "cv_text.txt")
cv_image_path = os.path.join("assets", "cv_image.jpg")

# Display the CV
display_cv(cv_text_path, cv_image_path)
