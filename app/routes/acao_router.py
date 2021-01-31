from typing import List
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from ..schema.Acao import AcaoSchema, AcaoCreate, AcaoUpdate
from ..services.acao_service import AcaoService
from ..helper.create_db_session import get_db

router = APIRouter(prefix="/acoes", tags=["acao"])


@router.post("/", response_model=AcaoSchema)
async def create_acao(infos_acao: AcaoCreate, db: Session = Depends(get_db)):
    api_acao = AcaoService(db)
    acao_cricao = api_acao.create_acao(infos_acao)
    return acao_cricao


@router.get("/", response_model=List[AcaoSchema])
async def list_acoes(request: Request, db: Session = Depends(get_db)):
    api_acao = AcaoService(db)
    acoes = api_acao.get_acoes()
    return acoes


@router.get("/{id_acao}", response_model=AcaoSchema)
async def get_acao(id_acao: int, db: Session = Depends(get_db)):
    api_apcao = AcaoService(db)
    acao_filtrada = api_apcao.get_acao(id_acao)
    return acao_filtrada


@router.put("/{id_acao}", response_model=AcaoSchema)
async def update_acao(
    id_acao: int, infos_acao: AcaoUpdate, db: Session = Depends(get_db)
):
    service_acao = AcaoService(db)
    acao = service_acao.update_acao(id_acao, infos_acao)
    return acao


@router.delete("/{id_acao}")
async def delete_acao(id_acao: int, db: Session = Depends(get_db)):
    service_acao = AcaoService(db)
    mensagem = service_acao.delete_acao(id_acao)
    return {"msg": mensagem}


@router.post("/teste")
async def get_form(request: Request, db: Session = Depends(get_db)):
    return {"corpo": request.body()}
