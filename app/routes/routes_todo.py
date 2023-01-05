from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from app.database.config import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.schemas_todo import TodoIn, Response
from app.database.config import get_db
from app.controllers.crud_todo import add_todo,delete_todo,update_status,update_todo,show_todos

router = APIRouter()


@router.get("/todos/")      
async def show_all_todos(db: Session = Depends(get_db)):
    todos = show_todos(db)
    return Response(status="OK",code="200", message="Success fetch all data",result=todos)
    
@router.post("/todos/",response_model=Response)
async def add_new_todo(req: TodoIn,db : Session = Depends(get_db)):
    todo = add_todo(req,db)
    return Response(status="OK",code="200",message = "Todo Added successfully").dict(exclude_none=True)

@router.delete("/todos/{id}")
async def delete_one_todo(id: int,db:Session = Depends(get_db)):
    delete_todo(id, db)
    return Response(status="Ok", code="200", message="Success delete todo").dict(exclude_none=True)

@router.patch("/todos/{id}")
async def update_one_todo(id: int,req: TodoIn, db : Session = Depends(get_db)):
    update_todo = update_todo(id ,req , db)
    return Response(status="Ok", code="200", message="Success update todo", result=update_todo)

@router.patch("/update_status/{id}")
async def status(id: int,status: str, db: Session = Depends(get_db)):
    update_status_todo = update_status(id, status, db)
    
    return Response(status="Ok", code="200", message="Success update status of todo", result=update_status_todo)
