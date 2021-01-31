from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserLogin(BaseModel):
    login: str
    senha: str


class UserCreate(UserLogin):
    nome: Optional[str] = "Estranho"
    email: str


class UserSchema(UserCreate):
    id_user: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    id_user: int
    login: Optional[str]
    senha: Optional[str]
    nome: Optional[str]
    email: Optional[str]
