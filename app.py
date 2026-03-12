from fastapi import FastAPI
from fastapi.responses import FileResponse
from validator import NotebookRequest
from main import synthesize_report
import os

app = FastAPI()


@app.get("/")
def health():
    return {"status": "Notebook Synthesis API running"}


@app.post("/generate_report")
def synthesize(request: NotebookRequest):

    result = synthesize_report(request)

    pdf_path = result["pdf_path"]
    filename = os.path.basename(pdf_path)

    return {
        "status": "success",
        "report_html": result["html"],
        "pdf_download_url": f"/download/{filename}"
    }


@app.get("/download/{filename}")
def download_report(filename: str):

    file_path = os.path.join("reports", filename)

    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=filename
    )