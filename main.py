from prompt import build_prompt
from model import generate_report


def synthesize_report(request):

    notebook_json = request.notebook
    user_query = request.user_query

    prompt = build_prompt(notebook_json, user_query)

    html_report = generate_report(prompt)

    # wrap HTML so browser/PDF engines render correctly
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

    return {
        "html": full_html
    }