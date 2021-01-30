from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    id_user: int
    login: str
    senha: str
    nome: Optional[str] = None
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    login: str
    senha: str
    nome: Optional[str] = "Estranho"
    email: str
