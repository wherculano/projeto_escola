from sqlalchemy import Column, Integer, String, Float
from database import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), index=True)
    idade = Column(Integer)
    nota_primeiro_semestre = Column(Float)
    nota_segundo_semestre = Column(Float)
    nome_professor = Column(String(255))
    numero_sala = Column(Integer)
