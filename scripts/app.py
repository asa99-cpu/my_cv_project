import streamlit as st
import os
from components import display_personal_details, display_skills, display_education, display_languages, display_internships

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
    st.markdown("### Contact Information", unsafe_allow_html=True)
    st.markdown("""
    **Email:** deman.najmadin90@gmail.com  
    **Phone:** +0750 710 40 32  
    **Date of Birth:** September 9, 1995  
    **Gender:** Female  
    **Nationality:** Kurdish
    """)

# Main content with columns
col1, col2 = st.columns([3, 1])

with col1:
    # Display Personal Details
    st.header("Personal Details")
    display_personal_details()

    st.header("Skills")
    display_skills()

    st.header("Education")
    display_education()

    st.header("Languages")
    display_languages()

    st.header("Internships")
    display_internships()

with col2:
    st.markdown("### Profile")
    st.markdown("""
    Enthusiastic and skilled individual with experience in multiple fields, including laboratory work, office tools, and video editing.
    Committed to learning and contributing positively to any professional environment.
    """)

    st.markdown("### Portfolio")
    st.markdown("For detailed work and projects, please visit [my portfolio](#).")

