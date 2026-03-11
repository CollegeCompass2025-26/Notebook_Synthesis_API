from fastapi import FastAPI
from validator import NotebookRequest
from main import synthesize_notebook

app = FastAPI()


@app.get("/")
def health():
    return {"status": "Notebook Synthesis API running"}


@app.post("/synthesize")
def synthesize(request: NotebookRequest):

    markdown = synthesize_notebook(request)

    return {
        "status": "success",
        "markdown": markdown
    }