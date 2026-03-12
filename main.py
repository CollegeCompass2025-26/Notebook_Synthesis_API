from prompt import build_prompt
from model import generate_report
from pdf_utils import html_to_pdf


def synthesize_report(request):

    notebook_json = request.notebook
    user_query = request.user_query

    prompt = build_prompt(notebook_json, user_query)

    html_report = generate_report(prompt)

    # wrap HTML
    full_html = f"""
    <html>
    <head>
        <title>Generated Notebook Report</title>
    </head>
    <body>
    {html_report}
    </body>
    </html>
    """

    # Convert HTML → PDF
    pdf_path = html_to_pdf(full_html)

    return {
        "html": html_report,
        "pdf_path": pdf_path
    }