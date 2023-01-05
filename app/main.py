from fastapi import FastAPI
from app.routes.routes_todo import router
from app.database.config import engine
from app.models.model_todo import Base, Status,Todo
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/todo", tags=["todo"])