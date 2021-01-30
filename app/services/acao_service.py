from typing import List
from sqlalchemy.orm import Session

from ..schema.Acao import AcaoCreate, AcaoSchema
from ..models.Acao import AcaoModel


class AcaoService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_acao(self, acao: AcaoCreate):
        new_acao = AcaoModel(
            codigo=acao.codigo,
            descricao=acao.descricao,
            setor=acao.setor,
            logo=acao.logo,
            url=acao.url,
        )
        self.db.add(new_acao)
        self.db.commit()
        self.db.refresh(new_acao)
        return new_acao

    def get_acoes(self) -> List[AcaoSchema]:
        acoes: List[AcaoSchema] = self.db.query(AcaoModel).all()
        return acoes

    def get_acao(self, id_acao) -> AcaoSchema:
        acao_filtred = (
            self.db.query(AcaoModel).filter(AcaoModel.id_acao == id_acao).first()
        )
        return acao_filtred
