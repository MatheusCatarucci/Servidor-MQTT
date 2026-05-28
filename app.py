from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from server import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# ──────────────────────────────────────────
# HOME
# ──────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    status = status()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"status":status}
    )


@app.post("/cadastro", response_class=HTMLResponse)
async def cadastro_hospede(
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cpf: str = Form(...),
):
    add_hospede(nome=nome, email=email, telefone=telefone, cpf=cpf)
    return RedirectResponse(url="/?success=1", status_code=303)


# ──────────────────────────────────────────
# DASHBOARD
# ──────────────────────────────────────────
@app.get("/hospedes", response_class=HTMLResponse)
async def hospedes(request: Request):
    hospedes = consulta_hospedes()
    return templates.TemplateResponse(
        request=request,
        name="hospedes.html",
        context={"hospedes": hospedes}
    )


# ──────────────────────────────────────────
# ENTRYPOINT — acessível na rede local
# ──────────────────────────────────────────
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)