from fastapi import FastAPI
from app.route import todo_router


app = FastAPI(debug=True)
app.include_router(todo_router)

