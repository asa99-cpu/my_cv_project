import streamlit as st
import os
from fpdf import FPDF

def display_cv(cv_text_path, cv_image_path):
    # Load CV text from file
    with open(cv_text_path, "r", encoding="utf-8") as file:
        cv_text = file.read()

    # Parse the text into sections based on double newlines.
    # We expect sections like: "Personal details", "Skills", etc.
    sections = cv_text.split("\n\n")
    cv_dict = {}
    for section in sections:
        lines = section.strip().split("\n")
        if lines:
            # Remove parentheses from the section title if present
            title = lines[0].strip().replace("(", "").replace(")", "")
            content = "\n".join(lines[1:]).strip()
            cv_dict[title] = content

    # --- Display in the Streamlit App ---
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
    Generate a one-page, two-column PDF.
      - Left column: Profile image and personal details.
      - Right column: Title and the sections (Skills, Education, Languages, Internships).
    """
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()

    # Define page dimensions and margins
    page_width = 210
    page_height = 297
    margin = 10
    usable_width = page_width - 2 * margin  # 190 mm
    usable_height = page_height - 2 * margin  # 277 mm

    # Define column widths and gap
    left_width = 60  # mm for left column
    gap = 10         # gap between columns
    right_width = usable_width - left_width - gap

    # Starting coordinates for left and right columns
    left_x = margin
    right_x = left_x + left_width + gap
    y_start = margin

    # --- LEFT COLUMN: Profile Image and Personal Details ---
    pdf.set_xy(left_x, y_start)
    if os.path.exists(cv_image_path):
        # Place the profile image. Assume a square image that fits the left column.
        image_size = left_width  # width and height in mm
        pdf.image(cv_image_path, x=left_x, y=y_start, w=left_width, h=image_size)
        y_after_image = y_start + image_size + 5  # 5 mm spacing after the image
    else:
        y_after_image = y_start

    # Print Personal Details (if available)
    pdf.set_xy(left_x, y_after_image)
    pdf.set_font("Arial", size=10)
    personal_details = cv_dict.get("Personal details", "Personal details not provided.")
    pdf.multi_cell(left_width, 5, personal_details, align="L")

    # --- RIGHT COLUMN: Main Content ---
    pdf.set_xy(right_x, y_start)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(right_width, 10, "CV - Derin Najmadin Mahamd", ln=True, align="C")
    # Draw a horizontal line below the title
    y_line = pdf.get_y()
    pdf.line(right_x, y_line, right_x + right_width, y_line)
    pdf.ln(5)

    # Sections to be printed on the right column (order is important)
    sections = ["Skills", "Education", "Languages", "Internships"]
    for section in sections:
        if section in cv_dict:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(right_width, 7, section, ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.multi_cell(right_width, 5, cv_dict[section])
            pdf.ln(3)  # small space between sections

    # Return PDF as bytes (encoded for download)
    return pdf.output(dest="S").encode("latin1")
