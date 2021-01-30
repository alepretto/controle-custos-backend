from fastapi import FastAPI, Depends, Form

from app.routes.users_route import router as user_router
from app.routes.categoria_router import router as categoria_router
from app.routes.transactions_router import router as transactions_router
from app.routes.acao_router import router as acao_router


app = FastAPI()

app.include_router(user_router)
app.include_router(categoria_router)
app.include_router(transactions_router)
app.include_router(acao_router)
