from typing import List
from sqlalchemy.orm import Session

from ..schema.User import CreateUser, UserSchema
from ..models.User import UserModel


class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def crate_user(self, user: CreateUser) -> UserSchema:
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