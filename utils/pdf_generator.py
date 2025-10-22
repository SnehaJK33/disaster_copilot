from fpdf import FPDF

def generate_pdf(summaries, filename="reports/daily_disaster_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for s in summaries:
        pdf.multi_cell(0, 10, f"{s.get('title', 'No Title')}\n{s.get('summary', '')}\n\n")

    pdf.output(filename)
