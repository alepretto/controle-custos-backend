from datetime import datetime
from pydantic import BaseModel


class AcaoSchema(BaseModel):
    id_acao: int
    codigo: str
    descricao: str
    url: str
    logo: str
    setor: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True