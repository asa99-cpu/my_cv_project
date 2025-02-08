import streamlit as st
from components import display_personal_details, display_skills, display_education, display_languages, display_internships

# Page configuration
st.set_page_config(
    page_title="Derin Najmadin Mahamd - CV",
    page_icon="📄",
    layout="wide"
)

# Template selection
cv_style = st.selectbox("Choose CV Template", ["Template 1", "Template 2", "Template 3", "Template 4", "Template 5"])

# Custom CSS based on selected template
with open(f"styles/{cv_style}.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header">
        <h1>Derin Najmadin Mahamd</h1>
        <h3>Graphic Designer & Full-Stack Developer</h3>
    </div>
""", unsafe_allow_html=True)

# Sidebar for image
with st.sidebar:
    st.image("assets/cv_image.jpg", width=200)
    st.markdown("### Contact Information")
    st.markdown("**Email:** deman.najmadin90@gmail.com")
    st.markdown("**Phone:** +0750 710 40 32")
    st.markdown("**Date of Birth:** September 9, 1995")
    st.markdown("**Gender:** Female")
    st.markdown("**Nationality:** Kurdish")

# Main content
st.markdown("<div class='section-header'>Personal Details</div>", unsafe_allow_html=True)
display_personal_details()

st.markdown("<div class='section-header'>Skills</div>", unsafe_allow_html=True)
display_skills()

st.markdown("<div class='section-header'>Education</div>", unsafe_allow_html=True)
display_education()

st.markdown("<div class='section-header'>Languages</div>", unsafe_allow_html=True)
display_languages()

st.markdown("<div class='section-header'>Internships</div>", unsafe_allow_html=True)
display_internships()
