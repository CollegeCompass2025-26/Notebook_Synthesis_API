def build_prompt(notebook_json, user_query):

    prompt = f"""
SYSTEM ROLE
You are a research analyst generating structured reports from notebook data.

TASK
Analyze the notebook and generate a research-style report.

NOTEBOOK DATA
{notebook_json}

USER QUERY
{user_query}

OUTPUT FORMAT
Return the result strictly as Markdown.
"""

    return prompt