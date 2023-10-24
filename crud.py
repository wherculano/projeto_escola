from sqlalchemy.orm import Session
from aluno_model import Aluno
from aluno_schema import AlunoCreate

def create_aluno(db: Session, aluno: AlunoCreate):
    db_aluno = Aluno(**aluno.dict())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno  # Retorne a instância do modelo SQLAlchemy, não é necessário um Pydantic

def get_aluno(db: Session, aluno_id: int):
    db_aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if db_aluno is None:
        return None

    return {
        "id": db_aluno.id,
        "nome": db_aluno.nome,
        "idade": db_aluno.idade,
        "nota_primeiro_semestre": db_aluno.nota_primeiro_semestre,
        "nota_segundo_semestre": db_aluno.nota_segundo_semestre,
        "nome_professor": db_aluno.nome_professor,
        "numero_sala": db_aluno.numero_sala
    }

def get_alunos(db: Session, skip: int = 0, limit: int = 100):
    db_alunos = db.query(Aluno).offset(skip).limit(limit).all()

    alunos = []
    for db_aluno in db_alunos:
        aluno_data = {
            "id": db_aluno.id,
            "nome": db_aluno.nome,
            "idade": db_aluno.idade,
            "nota_primeiro_semestre": db_aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": db_aluno.nota_segundo_semestre,
            "nome_professor": db_aluno.nome_professor,
            "numero_sala": db_aluno.numero_sala
        }
        alunos.append(aluno_data)

    return alunos


def update_aluno(db: Session, aluno_id: int, aluno: AlunoCreate):
    db_aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    for key, value in aluno.dict().items():
        setattr(db_aluno, key, value)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno  # Retorne a instância do modelo SQLAlchemy

def delete_aluno(db: Session, aluno_id: int):
    db_aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    db.delete(db_aluno)
    db.commit()
    return db_aluno  # Retorne a instância do modelo SQLAlchemy
