from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.database.connection import get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from passlib.context import CryptContext

# Cria o contexto de criptografia para senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    # Verifica se o email já existe
    db_user = session.exec(select(User).where(User.email == user.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    # ⚙️ >>> ADICIONE ESSAS DUAS LINHAS AQUI <<< ⚙️
    # Criptografa a senha antes de salvar
    hashed_password = pwd_context.hash(user.password)

    # Cria o usuário com a senha hasheada
    new_user = User(name=user.name, email=user.email, password=hashed_password)

    # Salva no banco
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


@router.get("/", response_model=list[UserResponse])
def list_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users
