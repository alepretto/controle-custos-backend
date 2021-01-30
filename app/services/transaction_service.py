from typing import List
from sqlalchemy.orm import Session

from ..schema.Transaction import TransactionCreate, TranscationSchema
from ..models.Transaction import TransactionModel


class TransactionService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_transaction(self, transaction: TransactionCreate) -> TranscationSchema:
        new_transaction = TransactionModel(
            id_user=transaction.id_user,
            id_categoria_transacao=transaction.id_categoria_transacao,
            id_acao=transaction.id_acao,
            tipo=transaction.tipo,
            valor=transaction.valor,
        )
        self.db.add(new_transaction)
        self.db.commit()
        self.db.refresh(new_transaction)
        return new_transaction

    def get_transactions(self):
        transactions: List[TranscationSchema] = self.db.query(TransactionModel).all()
        return transactions

    def get_transaction(self, id_transaction: int) -> TranscationSchema:
        return (
            self.db.query(TransactionModel)
            .filter(TransactionModel.id_transacao == id_transaction)
            .first()
        )
