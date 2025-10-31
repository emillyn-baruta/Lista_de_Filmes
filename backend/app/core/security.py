# backend/app/core/security.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from passlib.context import CryptContext
from sqlmodel import Session, select
from app.models.user import User
from app.database.connection import get_session
import os
from dotenv import load_dotenv

# =============================
# Configurações básicas
# =============================
load_dotenv()  # garante que .env seja carregado

SECRET_KEY = os.getenv("SECRET_KEY", "meusegredosuperseguro")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()


# =============================
# Funções de senha
# =============================
def verify_password(plain_password, hashed_password):
    """Compara senha digitada com a senha criptografada."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Gera o hash da senha antes de salvar no banco."""
    return pwd_context.hash(password)


# =============================
# Funções de token JWT
# =============================
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Gera o token JWT com tempo de expiração."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    """Valida e decodifica o token JWT."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


# =============================
# Obter usuário autenticado
# =============================
def get_current_user(
    token: str = Depends(security),
    session: Session = Depends(get_session)
):
    """Obtém o usuário logado a partir do token JWT."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        raise credentials_exception

    return user
