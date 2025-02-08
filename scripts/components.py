import streamlit as st

def display_cv(cv_text_path, cv_image_path):
    """Displays the CV image and extracted text in Streamlit."""
    
    # Layout: Image on Left, Text on Right
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(cv_image_path, caption="My CV", use_column_width=True)

    with col2:
        st.subheader("📜 Extracted CV Text")
        with open(cv_text_path, "r", encoding="utf-8") as file:
            cv_text = file.read()
        st.text_area("CV Content", cv_text, height=300, disabled=True)

    # Highlight Key Sections
    st.subheader("📌 Personal Details")
    st.write("""
    - **Name:** Derin Najmadin Mahamd  
    - **Email:** [deman.najmadin90@gmail.com](mailto:deman.najmadin90@gmail.com)  
    - **Phone:** 0750 710 40 32  
    - **Date of Birth:** September 9, 1995  
    - **Gender:** Female  
    - **Nationality:** Kurd  
    """)

    st.subheader("🛠 Skills")
    st.write("- Laboratory Technician\n- Microsoft Office\n- Translator\n- Video Editing\n- Sewing")

    st.subheader("🎓 Education")
    st.write("- **Bachelor's Degree in Science of Chemistry**")

    st.subheader("🗣 Languages")
    st.write("- Kurdish\n- Arabic\n- English\n- Persian")

    st.subheader("🏢 Internships")
    st.write("- Internship program of the Kurdistan Regional Government (2017)")


