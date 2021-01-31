from typing import List
from sqlalchemy.orm import Session

from ..schema.Categoria import CategoriaCreate, CategoriaSchema, CategoriaUpdate
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
        categoria_filtred = (
            self.db.query(CategoriaModel)
            .filter(CategoriaModel.id_categoria_transacao == id_categoria_transacao)
            .first()
        )
        return categoria_filtred

    def update_categoria_transacao(
        self, id_categori_transacao: int, infos_categoria: CategoriaUpdate
    ):
        infos_categoria = infos_categoria.dict(exclude_none=True)
        self.db.query(CategoriaModel).filter(
            CategoriaModel.id_categoria_transacao == id_categori_transacao
        ).update(infos_categoria)
        self.db.commit()

        categoria = (
            self.db.query(CategoriaModel)
            .filter(CategoriaModel.id_categoria_transacao == id_categori_transacao)
            .first()
        )
        return categoria

    def delete_categoria_trancacao(self, id_categoria: int):
        categoria = (
            self.db.query(CategoriaModel)
            .filter(CategoriaModel.id_categoria_transacao == id_categoria)
            .first()
        )
        if categoria:
            self.db.query(CategoriaModel).filter(
                CategoriaModel.id_categoria_transacao == id_categoria
            ).delete()
            self.db.commit()
            return "Categoria Excluida"
        else:
            raise ValueError("Categoria não encontrada")
