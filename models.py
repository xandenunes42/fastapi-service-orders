from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from typing import Optional

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefone = Column(String)

    ordens_servico = relationship("OrdemServico", back_populates="cliente")


# Modelo para a tabela de Ordens de Serviço
class OrdemServico(Base):
    __tablename__ = "ordens_servico"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))  # Relacionando com a tabela de clientes
    descricao = Column(String, nullable=False)
    data_abertura = Column(DateTime, default=datetime.utcnow)
    data_conclusao = Column(DateTime, nullable=True)
    status = Column(String, default="Em andamento")  # Status inicial

    # Relacionamento com o cliente (se existir)
    cliente = relationship("Cliente", back_populates="ordens_servico")
