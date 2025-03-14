from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from modeloenvios import modelenvio  # Asegúrate de que el modelo está bien importado

app = FastAPI(
    title='Examen Segundo Parcial',
    description='Noel Betanzos De La Cruz',
    version='6.6.6'
)

paquetes = [
    {"CP": "12345", "Destino": "Guadalajara", "Peso": 200},
    {"CP": "74532", "Destino": "Queretaro", "Peso": 360},
    {"CP": "47523", "Destino": "Oaxaca", "Peso": 489},
    {"CP": "12345", "Destino": "Oaxaca", "Peso": 489}  # Asegurar que CP sea string
]

# Endpoint para obtener un envío por CP
@app.get('/paquetes/{CP}', tags=['Envios'])
def obtener_envio(CP: str):
    for envio in paquetes:
        if envio["CP"] == CP:
            return {"Envío encontrado": envio}
    raise HTTPException(status_code=404, detail="Envío no encontrado")

# Endpoint para actualizar un envío existente
@app.put('/paquetes/{CP}', response_model=modelenvio, tags=['Envios'])
def actualizar_envio(CP: str, envio_update: modelenvio):
    for index, envio in enumerate(paquetes):
        if envio["CP"] == CP:
            paquetes[index] = envio_update.dict()  # Convertir Pydantic a diccionario
            return paquetes[index]
    raise HTTPException(status_code=404, detail="Envío no encontrado")
