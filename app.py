from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from server import *

app = FastAPI()
iniciar()

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

#-----------------------------------------------------

@app.get('/', response_class=HTMLResponse)
def home(request: Request):    
    return templates.TemplateResponse(

        estado_teste = {{
            "dispositvo":"on"
        }}

        request=request,
        name='home.html',
        context=estado_teste
    )