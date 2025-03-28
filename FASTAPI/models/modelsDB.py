from DB.conexion import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    _tablename_='tb_users'
    id=Column(Integer,primary_key=True, autoincrement="auto")
    name= Column(String)
    age= Column(Integer)
    email=Column(String)