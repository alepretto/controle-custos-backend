from datetime import datetime
import enum

from sqlalchemy import Column, Integer, Float, TIMESTAMP, ForeignKey, Enum
from sqlalchemy.orm import relationship
from config.database import Base


class EnumTipo(enum.Enum):
    outcome = "outcome"
    income = "income"


class TransactionModel(Base):
    __tablename__ = "transactions"

    id_transacao = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id_user"))
    id_categoria_transacao = Column(
        Integer, ForeignKey("categoriasTransacoes.id_categoria_transacao")
    )
    id_acao = Column(Integer, ForeignKey("acoes.id_acao"))
    tipo = Column(Enum(EnumTipo), nullable=False)
    valor = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())

    user = relationship("UserModel", back_populates="transactions")
    acao = relationship("AcaoModel", back_populates="transactions")
    categoriaTransacao = relationship("CategoriaModel", back_populates="transactions")
