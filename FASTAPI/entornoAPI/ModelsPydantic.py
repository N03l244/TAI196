from pydantic import BaseModel,Field,EmailStr
#Modelo para validaciones 
class modelUsuario(BaseModel):
    id:int = Field(...,gt=0, description="ID Unico y solo numeros positivos")
    nombre:str = Field(...,min_length=3,max_length=15, description="INombre debe contener solo letras y espacios")
    edad:int = Field(...,gt=0,le=133, description="La edad debe de ser mayor que 0")
    corre: EmailStr= Field(...,example="algo@algo.com", description="Revise la direccion de correo, debe ser un formato valido.")

