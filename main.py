from fastapi import FastAPI, Depends, Form

from app.routes.users_route import router as user_router


app = FastAPI()

app.include_router(user_router)
