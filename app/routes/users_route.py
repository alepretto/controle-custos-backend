from typing import List

from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session

from ..services.users_service import UserService
from ..schema.User import UserSchema, UserCreate, UserLogin, UserUpdate
from ..helper.create_db_session import get_db


router = APIRouter(prefix="/users", tags=["user"])


@router.post("/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> UserSchema:
    service_user = UserService(db)
    return service_user.crate_user(user)


@router.get("/", response_model=List[UserSchema])
async def list_users(db: Session = Depends(get_db)):
    service_user = UserService(db)
    resposta = service_user.get_users()

    return resposta


@router.get("/{id_user}")
async def get_user(id_user: int, db: Session = Depends(get_db)) -> UserSchema:
    service_user = UserService(db)
    user_filtred = service_user.get_user(id_user)
    return user_filtred


@router.put("/{id_user}")
async def update_user(
    id_user: int, infos_user: UserUpdate, db: Session = Depends(get_db)
):
    user_service = UserService(db)
    user_alterado = user_service.update_user(id_user, infos_user)
    return user_alterado


@router.delete("/{id_user}", status_code=201)
async def delete_user(id_user: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    deleted = user_service.delete_user(id_user)
    if deleted:
        return {"infos": "Usuário excluido"}


@router.post("/login")
async def user_login(user: UserLogin = Body(...), db: Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        return user_service.login_user(user)

    except ValueError as err:
        raise HTTPException(status_code=401, detail={"erro": str(err)})
