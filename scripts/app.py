import streamlit as st
import os
from scripts.components import display_cv

# Set page config
st.set_page_config(page_title="My CV", page_icon="📄", layout="centered")

# App Title
st.title("📄 My CV - Derin Najmadin Mahamd")

# Load and display the CV
cv_text_path = os.path.join("data", "cv_text.txt")
cv_image_path = os.path.join("assets", "cv_image.jpg")

# Run the display function from components.py
display_cv(cv_text_path, cv_image_path)

