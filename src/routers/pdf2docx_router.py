import os
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from starlette.exceptions import HTTPException

from pdf2docx import Converter

pdf2docx_router = APIRouter(prefix="/pdf2docx")

PDF_FOLDER = Path.cwd() / "pdf_folder"
PDF_FOLDER.mkdir(parents=True, exist_ok=True)

DOCX_FOLDER = Path.cwd() / "docx_folder"
DOCX_FOLDER.mkdir(parents=True, exist_ok=True)


def convert(pdf, docx):
    cv = Converter(pdf)
    print(DOCX_FOLDER / docx)
    cv.convert(DOCX_FOLDER / docx)
    cv.close()


async def createPdf(file):
    pdf_content = await file.read()
    file_path = PDF_FOLDER / file.filename
    with open(file_path, "wb") as f:
        f.write(pdf_content)
    return file_path


@pdf2docx_router.get("/convert")
async def pdftodocx(pdf: str, docx: str):
    if not os.path.exists(pdf):
        raise HTTPException(status_code=500, detail="Ruta no encontrada")

    try:
        convert(pdf, docx)
    except:
        raise HTTPException(status_code=500, detail="No se pudo crear el docx")

    return FileResponse(
        docx,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=docx,
    )


@pdf2docx_router.post("/upload")
async def upload(file: UploadFile = File()):
    file_path = await createPdf(file)
    return {"filename": file.filename, "saved_path": str(file_path)}


@pdf2docx_router.post("/")
async def upload_and_convert(docxname: str = Form(...), file: UploadFile = File()):
    file_path = await createPdf(file)
    if not os.path.exists(PDF_FOLDER / file_path):
        raise HTTPException(status_code=500, detail="No se pudo crear el pdf")

    try:
        print(file_path)
        convert(file_path, docxname)
        os.remove(file_path)
    except:
        raise HTTPException(status_code=500, detail="No se pudo crear el pdf")

    return FileResponse(
        DOCX_FOLDER / docxname,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=docxname,
    )
