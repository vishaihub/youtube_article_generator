from fpdf import FPDF

def create_pdf(content, output_path="outputs/article.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(output_path)
    return output_path