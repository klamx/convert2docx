import os

from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.exceptions import HTTPException
from pdf2docx import Converter

app = FastAPI()

def convert(pdf, docx):
  cv = Converter("./"+pdf)
  cv.convert(docx)
  cv.close()

@app.get("/pdf2docx")
async def pdftodocx(pdf, docx): 
  if not os.path.exists(pdf):
    raise HTTPException(status_code=500, detail="Ruta no encontrada")
  
  try:
    convert(pdf, docx)
  except:
    raise HTTPException(status_code=500, detail="No se pudo crear el pdf")

  return FileResponse(docx, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename=docx)