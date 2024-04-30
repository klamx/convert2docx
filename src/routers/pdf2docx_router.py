import os
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks
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

def remove_docx(path: str):
    os.remove(path)


@pdf2docx_router.post("/")
async def upload_and_convert(background_tasks: BackgroundTasks, docxname: str = Form(...), file: UploadFile = File()):
    file_path = await createPdf(file)
    if not os.path.exists(PDF_FOLDER / file_path):
        raise HTTPException(status_code=500, detail="No se pudo crear el pdf")

    try:
        print(file_path)
        convert(file_path, docxname)
        os.remove(file_path)
    except:
        raise HTTPException(status_code=500, detail="No se pudo crear el pdf")

    background_tasks.add_task(remove_docx, str(DOCX_FOLDER / docxname))
    
    return FileResponse(
        DOCX_FOLDER / docxname,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=docxname,
    )
