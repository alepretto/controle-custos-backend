from datetime import datetime
from pydantic import BaseModel


class CategoriaSchema(BaseModel):
    id_categoria_transacao: int
    nome: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True