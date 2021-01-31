from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schema.Transaction import TransactionCreate, TranscationSchema, TransactionUpdate
from ..services.transaction_service import TransactionService
from ..helper.create_db_session import get_db

router = APIRouter(prefix="/transactions", tags=["transaction"])


@router.post("/", response_model=TranscationSchema)
async def create_transaction(
    infos_transaction: TransactionCreate, db: Session = Depends(get_db)
):
    print(infos_transaction)
    transaction_service = TransactionService(db)
    transaction_created = transaction_service.create_transaction(infos_transaction)
    return transaction_created


@router.get("/", response_model=List[TranscationSchema])
async def list_transactions(db: Session = Depends(get_db)):
    transaction_service = TransactionService(db)
    transactions = transaction_service.get_transactions()
    return transactions


@router.get("/{id_transaction}", response_model=TranscationSchema)
async def get_transaction(id_transaction: int, db: Session = Depends(get_db)):
    transaction_service = TransactionService(db)
    transaction_filtred = transaction_service.get_transaction(id_transaction)
    return transaction_filtred


@router.put("/{id_transaction}", response_model=TranscationSchema)
async def update_transaction(
    id_transaction: int,
    infos_transaction: TransactionUpdate,
    db: Session = Depends(get_db),
):

    transaction_service = TransactionService(db)
    transaction = transaction_service.updated_transaction(
        id_transaction, infos_transaction
    )
    return transaction


@router.delete("/{id_transaction}", status_code=201)
async def delete_transaction(id_transaction: int, db: Session = Depends(get_db)):
    transaction_service = TransactionService(db)
    mensagem = transaction_service.delete_transaction(id_transaction)
    return {"msg": mensagem}
