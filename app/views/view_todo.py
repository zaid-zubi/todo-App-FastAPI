from fastapi import FastAPI
from app.routes import todo_router


app = FastAPI(debug=True)
app.include_router(todo_router)

