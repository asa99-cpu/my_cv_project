import streamlit as st
from scripts.components import display_personal_details, display_skills, display_education, display_languages, display_internships

# Page configuration
st.set_page_config(
    page_title="Derin Najmadin Mahamd - CV",
    page_icon="📄",
    layout="wide"
)

# Custom CSS
with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header Section
st.title("Derin Najmadin Mahamd")
st.markdown("---")

# Sidebar for image and contact information
with st.sidebar:
    st.image("assets/cv_image.jpg", width=200)
    st.markdown("### Contact Information")
    st.markdown("**Email:** deman.najmadin90@gmail.com")
    st.markdown("**Phone:** +0750 710 40 32")
    st.markdown("**Date of Birth:** September 9, 1995")
    st.markdown("**Gender:** Female")
    st.markdown("**Nationality:** Kurdish")

# Main Content Section with Two Columns
col1, col2 = st.columns([1, 2])

with col1:
    # Personal Details
    st.header("Personal Details")
    display_personal_details()

with col2:
    # Skills
    st.header("Skills")
    display_skills()

with col1:
    # Education
    st.header("Education")
    display_education()

with col2:
    # Languages
    st.header("Languages")
    display_languages()

with col1:
    # Internships
    st.header("Internships")
    display_internships()
