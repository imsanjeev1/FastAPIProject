from googletrans import Translator
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
######DB
from configuration.db_connect import conn
from migration.words import Words
from dbmodels.models import words
from fastapi import APIRouter
word=APIRouter()
templates = Jinja2Templates(directory="templates")

translator = Translator()
@word.get("/",response_class=HTMLResponse)
def index(request: Request):
    # conn.execute(words.select()).fetchall()
    # return conn.execute(words.select()).fetchall()
    return templates.TemplateResponse("page.html", {"request": request})

@word.post(path="/post_data")
async def extract_data_from_images(value=Form(),select_lang=Form()):
    # conn.execute(words.insert().values(
    #     input_word=word.input_word,
    #     converted_word = word.converted_word,
    #     lang_type = word.lang_type
    # ))
    # return conn.execute(words.select()).fetchall()
    translation = translator.translate(value, dest=select_lang)
    return str(translation.text)
#
