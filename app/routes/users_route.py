from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..services.users_service import UserService
from ..schema.User import UserSchema, CreateUser
from ..helper.created_db_session import get_db


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/")
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    service_user = UserService(db)
    return service_user.crate_user(user)


@router.get("/", response_model=List[UserSchema])
async def list_users(db: Session = Depends(get_db)):
    service_user = UserService(db)
    resposta = service_user.get_users()

    return resposta