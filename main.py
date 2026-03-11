from prompt import build_prompt
from model import generate_markdown


def synthesize_notebook(request):

    notebook_json = request.notebook
    user_query = request.user_query

    prompt = build_prompt(notebook_json, user_query)

    markdown_report = generate_markdown(prompt)

    print("\n----- GENERATED MARKDOWN -----\n")
    print(markdown_report)

    return markdown_report