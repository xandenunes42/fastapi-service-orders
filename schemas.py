from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

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


class OrdemServicoCreate(BaseModel):
    cliente_id: int
    descricao: str
    status: Optional[str] = "Em andamento"
    data_abertura: Optional[datetime] = None  # Alterado para None

    class Config:
        orm_mode = True

    def set_data_abertura(self):
        if not self.data_abertura:
            self.data_abertura = datetime.utcnow()
        return self

class OrdemServicoResponse(OrdemServicoCreate):
    id: int
    data_conclusao: Optional[datetime] = None

    class Config:
        orm_mode = True