from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from crud import create_aluno, get_aluno, get_alunos, update_aluno, delete_aluno
from aluno_model import Aluno
from aluno_schema import AlunoCreate, Aluno

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota padrão ("/") que redireciona para "/docs"
@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

# Create a new aluno
@app.post("/alunos/", response_model=Aluno)
def create_new_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    db_aluno = create_aluno(db, aluno)
    return db_aluno.__dict__  # Retorna o dicionário dos dados do aluno



# Get aluno by ID
@app.get("/alunos/{aluno_id}", response_model=Aluno)
def get_aluno_by_id(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = get_aluno(db, aluno_id)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno not found")
    return db_aluno

# Get all alunos
@app.get("/alunos/", response_model=list[Aluno])
def get_all_alunos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alunos = get_alunos(db, skip, limit)
    return alunos

# Update aluno
@app.put("/alunos/{aluno_id}", response_model=Aluno)
def update_existing_aluno(aluno_id: int, aluno: AlunoCreate, db: Session = Depends(get_db)):
    db_aluno = get_aluno(db, aluno_id)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno not found")
    return update_aluno(db, aluno_id, aluno)

# Delete aluno
@app.delete("/alunos/{aluno_id}", response_model=Aluno)
def delete_existing_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = get_aluno(db, aluno_id)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno not found")
    delete_aluno(db, aluno_id)
    return db_aluno
