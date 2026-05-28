from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from server import enviar_mensagem

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def pagina_inicial(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/transmitir")
async def transmitir_morse(palavra: str = Form(...)):
    texto = palavra.strip().upper()

    try:
        enviar_mensagem(texto)
        print(f"Mensagem enviada: {texto}")

    except Exception as erro:
        print(f"Erro MQTT: {erro}")

    return RedirectResponse(url="/", status_code=303)


# Bloco padrão para execução direta do script
if __name__ == "__main__":
    import uvicorn
    
    # Executa o servidor localmente na porta 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)