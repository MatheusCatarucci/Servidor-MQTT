from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import time

from server import *

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

log = [
    {"palavra": "SOS", "horario": "08:00"},
    {"palavra": "HELLO", "horario": "08:01"},
    {"palavra": "WORLD", "horario": "08:02"}
]


def registrar_log(palavra, horario):
    log.append({
        "palavra": palavra,
        "horario": horario
    })

def registrar_horario():
    horario_msg = time.localtime()
    return time.strftime("%H:%M:%S", horario_msg)

@app.post("/ascender")
def ascender():
    ascender_led()
    return RedirectResponse("/led", status_code=303)

@app.post("/apagar")
def apagar():
    apagar_led()
    return RedirectResponse("/led", status_code=303)

@app.get("/", response_class=HTMLResponse)
async def pagina_inicial(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/transmitir")
async def transmitir_morse(palavra: str = Form(...)):
    texto = palavra.strip().upper()

    try:
        enviar_mensagem(texto)

        registrar_log(
            palavra=texto,
            horario=registrar_horario()
        )

        print(f"Mensagem enviada: {texto}")

    except Exception as erro:
        print(f"Erro MQTT: {erro}")

    return RedirectResponse(url="/", status_code=303)


@app.get("/log", response_class=HTMLResponse)
async def registro(request: Request):
    try:
        return templates.TemplateResponse(
            request=request,
            name="log.html",
            context={"logs": log}
        )

    except Exception as erro:
        print(f"Erro ao renderizar log.html: {erro}")
        return RedirectResponse(url="/", status_code=302)

@app.get('/led', response_class=HTMLResponse)
def led(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='led.html'
    )

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )