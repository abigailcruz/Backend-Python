#Documentacion oficial: https://fastapi.tiangolo.com/es/
#Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI

app = FastAPI()

#URL Local: http://127.0.0.1:8000
@app.get("/")
async def root():
    return "Hola FastAPI!" 

#URL Local: http://127.0.0.1:8000/url
@app.get("/url")
async def root():
    return { "url_curso": "https://mouredev.com/python" } 

#Inicia el server: uvicorn main:app --reload
#Detener el server CTRL+C

#Documentacion Swagger: http://127.0.0.1:8000/docs
#Documentacion con Redocly: http://127.0.0.1:8000/redoc
