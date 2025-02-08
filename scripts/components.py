import streamlit as st
import os
from fpdf import FPDF

def display_cv(cv_text_path, cv_image_path):
    # Load CV text from file
    with open(cv_text_path, "r", encoding="utf-8") as file:
        cv_text = file.read()

    # Parse the text into sections based on double newlines.
    sections = cv_text.split("\n\n")
    cv_dict = {}
    for section in sections:
        lines = section.strip().split("\n")
        if lines:
            # Remove extra characters from the section title if present
            title = lines[0].strip().replace("(", "").replace(")", "")
            content = "\n".join(lines[1:]).strip()
            cv_dict[title] = content

    # --- Display in the Streamlit App (for preview) ---
    st.image(cv_image_path, width=250, caption="CV Profile Picture")
    st.markdown("## 📄 My CV - Derin Najmadin Mahamd")
    for section, content in cv_dict.items():
        st.markdown(f"### {section}")
        st.markdown(f"```{content}```")

    # --- Download buttons for TXT and PDF ---
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("📄 Download CV as TXT", data=cv_text, file_name="CV_Derin.txt", mime="text/plain")
    with col2:
        pdf_data = generate_pdf(cv_dict, cv_image_path)
        st.download_button("📄 Download CV as PDF", data=pdf_data, file_name="CV_Derin.pdf", mime="application/pdf")


def generate_pdf(cv_dict, cv_image_path):
    """
    Generate a modern, one-page, two-column PDF with advanced styling.
    The left panel is colored and contains your profile image and personal details.
    The right panel holds the main sections: Skills, Education, Languages, and Internships.
    """
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    # --- Define Colors ---
    left_bg_color = (40, 116, 166)  # A modern blue
    white = (255, 255, 255)
    dark_text = (50, 50, 50)

    # --- Left Panel Setup ---
    left_panel_width = 70  # in mm
    page_height = 297      # A4 height in mm

    # Draw the left panel background
    pdf.set_fill_color(*left_bg_color)
    pdf.rect(0, 0, left_panel_width, page_height, 'F')

    # Personal details (displayed in white text)
    pdf.set_text_color(*white)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_xy(10, 20)
    pdf.cell(50, 10, "Derin Najmadin", ln=1)
    pdf.cell(50, 10, "Mahamd", ln=1)

    pdf.set_font("Helvetica", "", 12)
    pdf.set_xy(10, 40)
    personal_info = (
        "Email: deman.najmadin90@gmail.com\n"
        "Phone: 0750 710 40 32\n"
        "DOB: September 9, 1995\n"
        "Gender: Female\n"
        "Nationality: Kurd"
    )
    pdf.multi_cell(50, 5, personal_info, align="L")

    # Insert profile image if available
    if os.path.exists(cv_image_path):
        # Place image below the personal details (adjust coordinates as needed)
        pdf.image(cv_image_path, x=10, y=80, w=50, h=50)

    # --- Right Panel Setup ---
    right_x = left_panel_width + 10  # start right panel with some margin
    pdf.set_text_color(*dark_text)
    y_position = 10

    # Header Title on the right panel
    pdf.set_xy(right_x, y_position)
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(130, 10, "CV - Derin Najmadin Mahamd", ln=1)
    
    # Draw a line below the header
    y_line = pdf.get_y() + 2
    pdf.set_line_width(0.5)
    pdf.line(right_x, y_line, right_x + 130, y_line)
    pdf.ln(8)

    # Sections to display on the right panel
    sections = ["Skills", "Education", "Languages", "Internships"]
    for section in sections:
        if section in cv_dict:
            pdf.set_xy(right_x, pdf.get_y())
            pdf.set_font("Helvetica", "B", 14)
            pdf.cell(130, 8, section, ln=1)
            pdf.set_font("Helvetica", "", 12)
            pdf.set_xy(right_x, pdf.get_y())
            pdf.multi_cell(130, 6, cv_dict[section])
            pdf.ln(4)

    # Return the PDF as bytes for download
    return pdf.output(dest="S").encode("latin1")
