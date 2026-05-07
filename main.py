from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import re

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def analyze_text(text):
    words = text.split()
    word_count = len(words)

    char_count = len(text)

    char_no_space = len(text.replace(" ", ""))

    sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in sentences if s.strip()]
    sentence_count = len(sentences)

    return word_count, char_count, char_no_space, sentence_count


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/analyse")
def analyze(request: Request, text: str = Form(...)):

    wc, cc, cns, sc = analyze_text(text)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "word_count": wc,
            "char_count": cc,
            "char_no_space": cns,
            "sentence_count": sc,
            "text": text
        }
    )