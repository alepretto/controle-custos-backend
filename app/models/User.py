from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from config.database import Base

from .Transaction import TransactionModel


class UserModel(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)
    login = Column(String(50), nullable=False)
    senha = Column(String(255), nullable=False)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())
    transactions = relationship("TransactionModel", back_populates="user")
