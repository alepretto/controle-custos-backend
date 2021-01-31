from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from ..schema.Categoria import CategoriaSchema, CategoriaCreate, CategoriaUpdate
from ..services.categorias_transactions_service import CategoriaTransacaoService
from ..helper.create_db_session import get_db

router = APIRouter(prefix="/categorias-transacoes", tags=["categoria_transacao"])


@router.post("/", response_model=CategoriaSchema)
def create_categoria(infos_categoria: CategoriaCreate, db: Session = Depends(get_db)):
    categoria_service = CategoriaTransacaoService(db)
    new_cateogria = categoria_service.create_categoria_tranacao(infos_categoria)
    return new_cateogria


@router.get("/", response_model=List[CategoriaSchema])
def lista_categorias(db: Session = Depends(get_db)):
    categoria_service = CategoriaTransacaoService(db)
    return categoria_service.list_categorias_transacoes()


@router.get("/{id_categoria}", response_model=CategoriaSchema)
def get_categoria_transacao(id_categoria: int, db: Session = Depends(get_db)):
    categoria_service = CategoriaTransacaoService(db)
    categoria_filtrada = categoria_service.get_categoria_transacao(id_categoria)
    return categoria_filtrada


@router.put("/{id_categoria}", response_model=CategoriaSchema)
def update_categoria_transacao(
    id_categoria: int, infos_categoria: CategoriaUpdate, db: Session = Depends(get_db)
):
    categoria_service = CategoriaTransacaoService(db)
    categoria = categoria_service.update_categoria_transacao(
        id_categoria, infos_categoria
    )
    return categoria


@router.delete("/{id_categoria}")
def delete_categoria(id_categoria: int, db: Session = Depends(get_db)):
    categoria_service = CategoriaTransacaoService(db)
    mensagem = categoria_service.delete_categoria_trancacao(id_categoria)
    return {"msg": mensagem}
