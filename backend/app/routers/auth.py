from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from pydantic import BaseModel
from app.database.connection import get_session
from app.models.user import User
from app.core.security import (
    verify_password,
    get_password_hash,
    create_access_token
)
import os
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["Auth"])

# ======================
# Schemas
# ======================
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str


# ======================
# Rotas
# ======================

@router.post("/register")
def register(user: UserCreate, session: Session = Depends(get_session)):
    """Rota para criar novo usuário"""
    existing_user = session.exec(select(User).where(User.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")

    hashed_pw = get_password_hash(user.password)
    new_user = User(name=user.name, email=user.email, password=hashed_pw)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message": "Usuário criado com sucesso", "user": new_user.email}


@router.post("/login")
def login(user: UserLogin, session: Session = Depends(get_session)):
    """Rota de login que gera o token JWT"""
    db_user = session.exec(select(User).where(User.email == user.email)).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")

    # Tempo de expiração do token (vem do .env)
    access_token_expires_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
    expires_delta = timedelta(minutes=access_token_expires_minutes)

    # Gera token com email como "sub"
    token = create_access_token(
        data={"sub": db_user.email},
        expires_delta=expires_delta
    )

    return {"access_token": token, "token_type": "bearer"}
