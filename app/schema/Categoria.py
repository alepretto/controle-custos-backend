from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CategoriaCreate(BaseModel):
    nome: str


class CategoriaSchema(CategoriaCreate):
    id_categoria_transacao: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CategoriaUpdate(BaseModel):
    nome: Optional[str]