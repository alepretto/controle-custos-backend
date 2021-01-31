from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class AcaoCreate(BaseModel):
    codigo: str
    descricao: str
    setor: str
    url: Optional[str]
    logo: Optional[str]


class AcaoSchema(AcaoCreate):
    id_acao: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AcaoUpdate(BaseModel):
    codigo: Optional[str]
    descricao: Optional[str]
    setor: Optional[str]
    url: Optional[str]
    logo: Optional[str]
