from fastapi import HTTPException,Request
from fastapi.security import HTTPBearer
from tokenGen import validateToken

class BearerJWT(HTTPBearer):
    async def __call__(self, request:Request):
        auth= await super()._call_(request)
        data= validateToken(auth.credentials)

        if not isinstance(data,dict):
            raise HTTPException(status_code=401,detail="Formato de token no valido")
        
        if data.get('email')!='ivan@example.com':
            raise HTTPException(status_code=403,detail="Credenciales No validas")