from pydantic import BaseModel

class AlunoCreate(BaseModel):
    nome: str
    idade: int
    nota_primeiro_semestre: float
    nota_segundo_semestre: float
    nome_professor: str
    numero_sala: int

class Aluno(BaseModel):
    nome: str
    idade: int
    nota_primeiro_semestre: float
    nota_segundo_semestre: float
    nome_professor: str
    numero_sala: int
