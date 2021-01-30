from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from config.database import Base


class AcaoModel(Base):
    __tablename__ = "acoes"

    id_acao = Column(Integer, primary_key=True)
    codigo = Column(String, nullable=False)
    descricao = Column(String)
    url = Column(String)
    logo = Column(String)
    setor = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now)
    transactions = relationship("TransactionModel", back_populates="acao")
