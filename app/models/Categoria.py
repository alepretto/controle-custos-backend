from datetime import datetime

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from config.database import Base


class CategoriaModel(Base):
    __tablename__ = "categoriasTransacoes"

    id_categoria_transacao = Column(Integer, primary_key=True)
    nome = Column(String)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date, default=datetime.now(), onupdate=datetime.now())
    transaction = relationship("Transaction", backref="categoriaTransacao")
