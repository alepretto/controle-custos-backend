from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from app.routes.users_route import router as user_router
from app.routes.categoria_router import router as categoria_router
from app.routes.transactions_router import router as transactions_router
from app.routes.acao_router import router as acao_router

from app.auth.middleware_auth import auth_user


app = FastAPI()

app.add_middleware(BaseHTTPMiddleware, dispatch=auth_user)
app.include_router(user_router)
app.include_router(categoria_router)
app.include_router(transactions_router)
app.include_router(acao_router)
