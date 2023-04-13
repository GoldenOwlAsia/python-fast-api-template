from fastapi import FastAPI
from app.api.v1.routes import users

app = FastAPI()
app.include_router(router=users.router)
