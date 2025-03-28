
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from ModelsPydantic import modelUsuario, modelAuth
from tokenGen import createToken
from middlewares import BearerJWT
from DB.conexion import Session,engine, Base
from models.modelsDB import User

app= FastAPI(
    title='Mi primer API 196',
    description='Noel Betanzos De La Cruz',
    version= '1.1.1'
)
#Se encarga de levantar las Tables de la DB
usuarios=[
    {"id":1, "nombre":"Noel", "edad": 20, "correo":"Noel@example.com"},
    {"id":2, "nombre":"Ivan", "edad": 37, "correo":"Ivan@example.com"},
    {"id":3, "nombre":"Sergio", "edad": 20, "correo":"Sergio@example.com"},
    {"id":4, "nombre":"Preciado", "edad": 21, "correo":"Preciado@example.com"},
]


@app.get('/',tags=['Inicio'])
def main():
    return {'hola FastApi','Noel'}

#endPoint para generar un token
@app.post('/auth/',tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.correo == 'Noel@example.com' and autorizado.passw == '1234567890':
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return{"Aviso":"Usuario no Autorizado"}
    

#endPoint Consultar todos
@app.get('/usuarios',dependencies=[ Depends(BearerJWT())],response_model= List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

#endPoint para agrregar usuarios
@app.post('/usuario/',response_model= modelUsuario,tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo: modelUsuario):
    for usr in usuarios: 
        if usr["id"] == usuarionuevo.id: 
            raise HTTPException(status_code=400, detail="El id ya esta registrado") 
    usuarios.append(usuarionuevo) 
    return usuarionuevo 

#endPoint para PUT
@app.put("/usuario/{id}",response_model= modelUsuario, tags=["Operaciones CRUD"])
def actualizar(id: int, usuario_update: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]= usuario_update.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=404, detail="ID no encontrado")

#endPoint para Delete
@app.delete("/usuario/{id}", tags=["Operaciones CRUD"])
def eliminar(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {"Usuario eliminado":id}
    raise HTTPException(status_code=404, detail="ID no encontrado")