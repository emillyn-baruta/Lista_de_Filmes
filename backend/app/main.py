from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# ----------------------------
# 🔧 Carregar variáveis de ambiente
# ----------------------------
env_path = r"C:\Users\Dell\desafio-elite-dev\backend\.env"
load_dotenv(dotenv_path=env_path)

print("✅ DATABASE_URL:", os.getenv("DATABASE_URL"))
print("✅ TMDB_API_KEY:", os.getenv("TMDB_API_KEY"))

# ----------------------------
# 🚀 Inicialização do FastAPI
# ----------------------------
from app.database.connection import create_db_and_tables
from app.routers import user_router, movies as movies_router, favorite_router, auth

app = FastAPI(
    title="Desafio Elite Dev API 🚀",
    description="API do desafio Full Stack — com rotas de usuários, filmes e favoritos.",
    version="1.0.0",
    debug=True
)

# ----------------------------
# 🌍 CORS - liberar acesso total (para testes locais)
# ----------------------------
origins = ["*"]  # 👈 Permite acesso de qualquer origem durante o desenvolvimento

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# 🗄️ Inicialização do banco
# ----------------------------
@app.on_event("startup")
async def on_startup():
    try:
        create_db_and_tables()
        print("✅ Banco de dados inicializado com sucesso!")
    except Exception as e:
        print("❌ Erro ao inicializar banco:", e)

# ----------------------------
# 🌐 Rota base
# ----------------------------
@app.get("/")
def root():
    return {"message": "🚀 Servidor ativo com sucesso e banco de dados conectado!"}

# ----------------------------
# 📦 Rotas principais
# ----------------------------
app.include_router(user_router.router)
app.include_router(movies_router.router)
app.include_router(favorite_router.router)
app.include_router(auth.router)
