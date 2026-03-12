from weasyprint import HTML
import os
import uuid


def html_to_pdf(html_content):

    # create unique file name
    pdf_name = f"report_{uuid.uuid4().hex}.pdf"
    pdf_path = os.path.join("reports", pdf_name)

    # ensure folder exists
    os.makedirs("reports", exist_ok=True)

    # convert html -> pdf
    HTML(string=html_content).write_pdf(pdf_path)

    return pdf_path