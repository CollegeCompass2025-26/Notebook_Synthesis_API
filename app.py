from fastapi import FastAPI, Response
from validator import NotebookRequest, PDFRequest
from main import synthesize_report
from pdf_utils import html_to_pdf

app = FastAPI()


@app.post("/generate_report")
def generate_report(request: NotebookRequest):

    result = synthesize_report(request)

    html = result["html"]

    return {
        "html": html,
        "pdf_download_url": "/download_pdf"
    }


@app.post("/download_pdf")
def download_pdf(request: PDFRequest):

    pdf_bytes = html_to_pdf(request.html)

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=report.pdf"
        }
    )