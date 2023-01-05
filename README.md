# fast-todo app


* User can add , update , delete todo , get all todos , update status of one todo.

1. Clone the project on your local machine.

2. Install venv :
py -m venv venv

3. Activate the venv:
.\venv\Scripts\activate

4. To run the project enter:
uvicorn app.main:app --reload

- Note : Enter your database URL in SQLALCHEMY_DATABASE_URL
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5432/DBname"
