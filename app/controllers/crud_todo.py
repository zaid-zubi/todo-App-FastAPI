from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.config import SessionLocal, engine, get_db,Base
from app.models.model_todo import Todo
from app.schemas.schemas_todo import TodoIn




def show_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos

def add_todo(req: TodoIn, db: Session = Depends(get_db)):
    todo = Todo(**req.dict())
    print(todo)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter_by(id=id).first()
    db.delete(todo)
    db.commit()
    return {"message": "todo deleted successfull"}


def update_todo(id: int, req: TodoIn, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter_by(id=id).first()
    todo_data = req.dict(exclude_unset=True)
    for key, value in todo_data.items():
        print(f'key : {key} || value : {value}')
        setattr(todo, key, value)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_status(id: int, status: str, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter_by(id=id).first()
    todo.status = status
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

