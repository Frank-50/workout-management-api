#importa a biblioteca do fastapi
from fastapi import FastAPI
#cria a variavel que inicia os endpoints das rotas
app = FastAPI()

# importa a variavel router do arquivo routes que esta dentro da pasta api
from app.api.routes import router
#define que app ser atreibuido a nova variavel router
app.include_router(router)