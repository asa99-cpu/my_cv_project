import streamlit as st
import os
from fpdf import FPDF  # For PDF generation

def display_cv(cv_text_path, cv_image_path):
    # Load CV text
    with open(cv_text_path, "r", encoding="utf-8") as file:
        cv_text = file.read()

    # Split CV sections
    sections = cv_text.split("\n\n")  # Splitting by double newlines
    cv_dict = {}

    for section in sections:
        lines = section.strip().split("\n")
        if lines:
            title = lines[0].strip().replace("(", "").replace(")", "")
            content = "\n".join(lines[1:])
            cv_dict[title] = content

    # Display CV Image
    st.image(cv_image_path, width=250, caption="CV Profile Picture")

    # Display CV Details
    st.markdown("## 📄 My CV - Derin Najmadin Mahamd")
    for section, content in cv_dict.items():
        st.markdown(f"### {section}")
        st.markdown(f"```{content}```")

    # Download buttons
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("📄 Download CV as TXT", data=cv_text, file_name="CV_Derin.txt", mime="text/plain")

    with col2:
        pdf_data = generate_pdf(cv_dict)  # Generate PDF
        st.download_button("📄 Download CV as PDF", data=pdf_data, file_name="CV_Derin.pdf", mime="application/pdf")

def generate_pdf(cv_dict):
    """Generate a modern, stylish PDF file from CV details."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()

    # Set fonts for headings and body
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "CV - Derin Najmadin Mahamd", ln=True, align="C")
    
    # Draw a line under the header
    pdf.line(10, 20, 200, 20)

    # Add space after title
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    
    # Personal Information (Name, Email, Phone, etc.)
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "Personal Information", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Name: Derin Najmadin Mahamd", ln=True)
    pdf.cell(0, 10, f"Email: deman.najmadin90@gmail.com", ln=True)
    pdf.cell(0, 10, f"Phone: 0750 710 40 32", ln=True)
    pdf.cell(0, 10, f"Date of Birth: September 9, 1995", ln=True)
    pdf.cell(0, 10, f"Gender: Female", ln=True)
    pdf.cell(0, 10, f"Nationality: Kurd", ln=True)

    # Draw a line after personal info
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    # Add space after personal info
    pdf.ln(10)

    # Loop through the CV sections
    for section, content in cv_dict.items():
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(0, 10, section, ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, content)

        # Draw a line after each section
        pdf.ln(5)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(10)

    return pdf.output(dest="S").encode("latin1")  # Return as bytes
