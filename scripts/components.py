import streamlit as st

def display_personal_details():
    st.markdown("""
    <ul class="details">
        <li><strong>Name:</strong> Derin Najmadin Mahamd</li>
        <li><strong>Email:</strong> deman.najmadin90@gmail.com</li>
        <li><strong>Phone:</strong> +0750 710 40 32</li>
        <li><strong>Date of Birth:</strong> September 9, 1995</li>
        <li><strong>Gender:</strong> Female</li>
        <li><strong>Nationality:</strong> Kurdish</li>
    </ul>
    """, unsafe_allow_html=True)

def display_skills():
    st.markdown("""
    <ul class="skills">
        <li><strong>Laboratory Technician</strong></li>
        <li><strong>Microsoft Office</strong></li>
        <li><strong>Translator</strong></li>
        <li><strong>Video Editing</strong></li>
        <li><strong>Sewing</strong></li>
    </ul>
    """, unsafe_allow_html=True)

def display_education():
    st.markdown("""
    <ul class="education">
        <li><strong>Bachelor Degree in Science of Chemistry</strong></li>
    </ul>
    """, unsafe_allow_html=True)

def display_languages():
    st.markdown("""
    <ul class="languages">
        <li><strong>Kurdish</strong></li>
        <li><strong>Arabic</strong></li>
        <li><strong>English</strong></li>
        <li><strong>Persian</strong></li>
    </ul>
    """, unsafe_allow_html=True)

def display_internships():
    st.markdown("""
    <ul class="internships">
        <li><strong>Internship Program of the Kurdistan Regional Government (2017)</strong></li>
    </ul>
    """, unsafe_allow_html=True)
