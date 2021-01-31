from typing import List
from sqlalchemy.orm import Session

from ..schema.Transaction import TransactionCreate, TranscationSchema, TransactionUpdate
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
        try:
            return (
                self.db.query(TransactionModel)
                .filter(TransactionModel.id_transacao == id_transaction)
                .first()
            )
        except:
            raise ValueError("Transação não encontrada")

    def updated_transaction(
        self, id_transaction: int, infos_transaction: TransactionUpdate
    ):
        infos_transaction = infos_transaction.dict(exclude_none=True)
        self.db.query(TransactionModel).filter(
            TransactionModel.id_transacao == id_transaction
        ).update(infos_transaction)
        self.db.commit()
        transaction = (
            self.db.query(TransactionModel)
            .filter(TransactionModel.id_transacao == id_transaction)
            .first()
        )
        return transaction

    def delete_transaction(self, id_transaction: int):
        transaction = (
            self.db.query(TransactionModel)
            .filter(TransactionModel.id_transacao == id_transaction)
            .first()
        )
        if transaction:
            self.db.query(TransactionModel).filter(
                TransactionModel.id_transacao == id_transaction
            ).delete()
            self.db.commit()
            return "Transação excluida"
        else:
            raise ValueError("Transação não encontrada")
