import pdfkit

# path inside Linux container
config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")

def html_to_pdf(html_content: str):

    pdf_bytes = pdfkit.from_string(
        html_content,
        False,  # return bytes instead of writing file
        configuration=config
    )

    return pdf_bytes