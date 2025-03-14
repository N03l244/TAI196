from pydantic import BaseModel, Field

# Modelo para validaciones de envío
class modelenvio(BaseModel):
    CP: str = Field(..., min_length=5, description="Ingrese el CP de como mínimo 5 caracteres")
    Destino: str = Field(..., min_length=6, description="Ingrese el destino del paquete de como mínimo 6 caracteres")
    Peso: int = Field(..., gt=0, le=500, description="El peso del paquete debe ser entre 1 y 500 gramos")
    
# Modelo para autenticación (solo CP por ahora)
class modelAuth(BaseModel):
    CP: str
