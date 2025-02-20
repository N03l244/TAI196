from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title='API de Gestión de Tareas 196',
    description='Noel Betanzos De La Cruz',
    version= '1.0.0.0'
)
tareas = [
    {"id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes de TAI", "vencimiento": "14-02-24", "estado": "completada"},
    {"id": 2, "titulo": "Desarrollar API de tareas", "descripcion": "Crear endpoints para CRUD (Create, Read, Update, Delete)", "vencimiento": "20-02-24", "estado": "no completada"},
    {"id": 3, "titulo": "Hacer ejercicio", "descripcion": "Ir al gimnasio y realizar rutina de fuerza", "vencimiento": "22-02-24", "estado": "no completada"},
    {"id": 4, "titulo": "Actualizar el CV", "descripcion": "Agregar experiencia en Flask y Jinja2", "vencimiento": "25-02-24", "estado": "no completada"},
    {"id": 5, "titulo": "Comprar víveres", "descripcion": "Leche, huevos, pan, frutas y verduras", "vencimiento": "19-02-24", "estado": "completada"},
    {"id": 6, "titulo": "Preparar presentación", "descripcion": "Finalizar diapositivas para la exposición de reingeniería", "vencimiento": "23-02-24", "estado": "no completada"},
    {"id": 7, "titulo": "Pagar servicios", "descripcion": "Luz, agua e internet", "vencimiento": "28-02-24", "estado": "no completada"},
    {"id": 8, "titulo": "Leer un libro", "descripcion": "Terminar el capítulo 5 de 'Clean Code'", "vencimiento": "26-02-24", "estado": "no completada"},
    {"id": 9, "titulo": "Enviar reportes", "descripcion": "Subir informe mensual a la plataforma", "vencimiento": "21-02-24", "estado": "completada"},
    {"id": 10, "titulo": "Revisar correos", "descripcion": "Responder a los pendientes del equipo de desarrollo", "vencimiento": "18-02-24", "estado": "completada"}
]

#endPoint Obtener todas las tareas.
@app.get('/tareas', tags=['To-Do List'])
def ObtenerTodos():
    return {"Tareas Registrados. ": tareas}


#endPoint Obtener la tarea por ID.
@app.get('/tareas/{id}', tags=['To-Do List'])
def ObtenerTodos(id:int):
    for tarea in tareas:
        if tarea["id"] == id:
            return {"Tarea encontrada": tarea}
    raise HTTPException(status_code=404, detail="Tarea no encontrado")

#endPoint para Crear una nueva tarea.
@app.post('/tareas/',tags=['To-Do List'])
def AgregarUsuario(tareanuevo: dict ):
    for tarea in tareas: 
        if tarea["id"] == tareanuevo.get("id"): 
            raise HTTPException(status_code=400, detail="El id ya esta registrado") 
    tareas.append(tareanuevo) 
    return tareanuevo 

#endPoint para Actualizar una tarea existente.
@app.put("/tareas/{id}", tags=["To-Do List"])
def actualizar(id: int, tarea_update: dict):
    for index, tra in enumerate(tareas):
        if tra["id"] == id:
            tareas[index].update(tarea_update)
            return tareas[index]
    raise HTTPException(status_code=404, detail="ID no encontrado")

#endPoint para Eliminar una tarea.
@app.delete("/tareas/{id}", tags=["To-Do List"])
def eliminar(id: int):
    for index, tra in enumerate(tareas):
        if tra["id"] == id:
            tareas.pop(index)
            return {"Usuario eliminado":id}
    raise HTTPException(status_code=404, detail="ID no encontrado")
