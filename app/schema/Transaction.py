from enum import Enum
from datetime import datetime

from fastapi import Form
from pydantic import BaseModel
from typing import Optional


class EnumTipo(str, Enum):
    outcome = "outcome"
    income = "income"


class TranscationSchema(BaseModel):
    id_transacao: int
    id_user: int
    id_categoria_transacao: int
    id_acao: Optional[int] = None
    tipo: EnumTipo
    valor: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class TransactionCreate(BaseModel):
    id_user: int
    id_categoria_transacao: int
    id_acao: Optional[int] = None
    tipo: EnumTipo
    valor: float