from pydantic import BaseModel, EmailStr

class ClienteBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True
