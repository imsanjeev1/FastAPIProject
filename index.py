from fastapi import FastAPI
from main import word
app = FastAPI()
app.include_router(word)
#
# @app.get("/")
# def read_file():
#     return {"msg":"Return Data"}