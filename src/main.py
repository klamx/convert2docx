from typing import Union
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

from src.routers.pdf2docx_router import pdf2docx_router

app = FastAPI()

if __name__ == "__main__":

    app.include_router(router=pdf2docx_router, prefix="/api/v1")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/", tags=["Home"])
    def home():
        return PlainTextResponse(content="Home", status_code=200)
