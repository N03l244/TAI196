from fastapi.responses import JSONResponse
from ModelsPydantic import modelauth
from tokenGen import createToken
from fastapi import APIRouter

routerAuth= APIRouter()

@routerAuth.post('/auth', tags=['Autentificacion'])
def login(autorizado:modelauth):
    if autorizado.corre == 'Noel@Bet.com' and autorizado.passw == '123456789':
        token: str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return{"aviso":"usuario no autorizado"}