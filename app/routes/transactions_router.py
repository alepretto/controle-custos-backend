from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schema.Transaction import TransactionCreate, TranscationSchema
from ..services.transaction_service import TransactionService
from ..helper.create_db_session import get_db

router = APIRouter(prefix="/transactions", tags=["transaction"])


@router.post("/", response_model=TranscationSchema)
def create_transaction(
    infos_transaction: TransactionCreate, db: Session = Depends(get_db)
):
    transaction_service = TransactionService(db)
    transaction_created = transaction_service.create_transaction(infos_transaction)
    return transaction_created


@router.get("/", response_class=List[TranscationSchema])
def list_transactions(db: Session = Depends(get_db)):
    transaction_service = TransactionService(db)
    transactions = transaction_service.get_transactions()
    return transactions


@router.get("/{id_transaction}", response_model=TranscationSchema)
def get_transaction(id_transaction: int, db: Session = Depends(get_db)):
    transaction_service = TransactionService(db)
    transaction_filtred = transaction_service.get_transaction(id_transaction)
    return transaction_filtred