from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schema.Acao import AcaoSchema, AcaoCreate
from ..services.acao_service import AcaoService
from ..helper.create_db_session import get_db

router = APIRouter(prefix="/acoes", tag=["acao"])


@router.post("/", response_model=AcaoSchema)
async def create_acao(infos_acao: AcaoCreate, db: Session = Depends(get_db)):
    api_acao = AcaoService(db)
    acao_cricao = api_acao.create_acao(infos_acao)
    return acao_cricao


@router.get("/", response_model=List[AcaoSchema])
async def list_acoes(db: Session = Depends(get_db)):
    api_acao = AcaoService(db)
    api_acao.get_acoes()
    return api_acao


@router.get("/{id_acao}", response_model=AcaoSchema)
async def get_acao(id_acao: int, db: Session = Depends(get_db)):
    api_apcao = AcaoService(db)
    acao_filtrada = api_apcao.get_acao(id_acao)
    return acao_filtrada
