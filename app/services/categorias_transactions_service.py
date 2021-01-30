from typing import List
from sqlalchemy.orm import Session

from ..schema.Categoria import CategoriaCreate, CategoriaSchema
from ..models.Categoria import CategoriaModel


class CategoriaTransacaoService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_categoria_tranacao(
        self, categoria_transacao: CategoriaCreate
    ) -> CategoriaSchema:
        new_categoria_transacao = CategoriaModel(nome=categoria_transacao.nome)
        self.db.add(new_categoria_transacao)
        self.db.commit()
        self.db.refresh(new_categoria_transacao)
        return new_categoria_transacao

    def list_categorias_transacoes(self) -> List[CategoriaSchema]:
        transacoes = self.db.query(CategoriaModel).all()
        return transacoes

    def get_categoria_transacao(self, id_categoria_transacao: int) -> CategoriaSchema:
        categoria_filtred = self.db.query(CategoriaModel).filter(
            CategoriaModel.id_categoria_transacao == id_categoria_transacao
        )
        return categoria_filtred
