from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TranscationSchema(BaseModel):
    id_transacao: int
    id_user: int
    id_categoria_transacao: int
    id_acao: Optional[int] = None
    tipo: str
    valor: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class TransactionCreate(BaseModel):
    id_user: int
    id_categoria_transacao: int
    id_acao: Optional[int] = None
    tipo: str
    valor: float