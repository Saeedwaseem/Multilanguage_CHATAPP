from fastapi import FastAPI
from models.model import *
from utils.translator import translate

app = FastAPI()






@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/translate")
def translate_email(req: TranslateBody):
    return translate(req.src, req.dst, req.data)