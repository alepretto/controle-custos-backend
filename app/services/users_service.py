from typing import Dict, List
from sqlalchemy.orm import Session

from ..schema.User import UserCreate, UserSchema, UserUpdate, UserLogin
from ..models.User import UserModel
from ..auth.auth_hendler import signJWT


class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def crate_user(self, user: UserCreate) -> UserSchema:
        db_user = UserModel(
            login=user.login, senha=user.senha, nome=user.nome, email=user.email
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_users(self, skip: int = 0, limit: int = 1000):
        list_users: List[UserSchema] = self.db.query(UserModel).all()
        return list_users

    def get_user(self, id_user):
        return self.db.query(UserModel).filter(UserModel.id_user == id_user).first()

    def update_user(self, infos_user: UserUpdate):
        usuario_selecionado = (
            self.db.query(UserModel)
            .filter(UserModel.id_user == infos_user.id_user)
            .first()
        )
        pass

    def login_user(self, user_info: UserLogin):
        user = (
            self.db.query(UserModel).filter(UserModel.login == user_info.login).first()
        )
        if not user:
            raise ValueError("Login não encontrado")
        if user.senha != user_info.senha:
            raise ValueError("Senha inválida!")

        access_token = signJWT(user.id_user)
        access_token["user"] = user
        return access_token
