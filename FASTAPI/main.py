
from fastapi import FastAPI
from typing import Optional

app= FastAPI(
    title='Mi primer API 196',
    description='Noel Betanzos De La Cruz',
    version= '1.0.1'
)
usuarios=[
    {"id":1, "nombre":"Noel", "edad": 20},
    {"id":2, "nombre":"Ivan", "edad": 37},
    {"id":3, "nombre":"Sergio", "edad": 20},
    {"id":4, "nombre":"Preciado", "edad": 21},
]

@app.get('/',tags=['Inicio'])
def main():
    return {'hola FastApi','Noel'}

@app.get('/promedio',tags=['Mi Calificacion TAI'])
def promedio():
    return 10
#endPoint Parametro obligatorio
@app.get('/usuario/{id}',tags=['Parametro Obligatorio'])
def consultaUsuario(id:int):
    #conectamos BD
    #hacemos consulta, retornamos resultset
    return{"Se encontro el usuario":id} 


#endPoint Parametro opcional
@app.get('/usuario/',tags=['Parametro opcional'])
def consultaUsuario2(id:Optional[int]= None):
        if id is not None:
            for usuario in usuarios:
                if usuario["id"] == id:
                    return{"mensaje":"Usuario encontrado", "usuario":usuario}
            return{"mensaje":f"No encontre el ID: {id}"}
        else:
            return{"mensaje": "No se proporciono un Id"}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}