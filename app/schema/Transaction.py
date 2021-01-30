from datetime import datetime
from pydantic import BaseModel


class TranscationSchema(BaseModel):
    id_transacao: int
    id_user: int
    id_categoria_transacao: int
    id_acao: int
    tipo: str
    valor: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True