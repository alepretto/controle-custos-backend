from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id_user: int
    login: str
    senha: str
    nome: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
