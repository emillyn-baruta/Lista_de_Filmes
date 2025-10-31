# backend/app/database/connection.py
import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv


# Caminho absoluto para o arquivo .env (ajuste se estiver em outro local)
env_path = r"C:\Users\Dell\desafio-elite-dev\backend\.env"
load_dotenv(dotenv_path=env_path)

# Pega a URL do banco
DATABASE_URL = os.getenv("DATABASE_URL")

# DEBUG rápido — remova depois
print("DATABASE_URL:", DATABASE_URL)

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não encontrada no .env")

# Cria o engine (conexão com PostgreSQL)
engine = create_engine(DATABASE_URL, echo=False)  # echo=True mostra os comandos SQL no terminal

# Cria o banco e as tabelas
def create_db_and_tables():
    try:
        # Importa todos os modelos usados nas tabelas
        from app.models import user, favorite

        # Cria todas as tabelas registradas nos models
        SQLModel.metadata.create_all(engine)
        print("Tabelas criadas com sucesso!")
    except Exception as e:
        print("Erro ao criar tabelas:", e)

# Dependência para abrir sessão (usar em routers com Depends)
def get_session():
    with Session(engine) as session:
        yield session

