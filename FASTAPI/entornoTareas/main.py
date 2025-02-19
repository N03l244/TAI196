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