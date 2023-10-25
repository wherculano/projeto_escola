from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Substitua as informações abaixo pelas configurações do seu servidor MySQL
MYSQL_USER = "root"
MYSQL_PASSWORD = "nova_senha"
MYSQL_HOST = "172.17.0.2"
MYSQL_DB = "projeto_escola"

# Crie a URL de conexão do SQLAlchemy para o MySQL com o driver mysql-connector-python
DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
