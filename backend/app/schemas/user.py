from pydantic import BaseModel, EmailStr

# Schema base (campos que todo User tem)
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Schema para criação de usuário (inclui senha)
class UserCreate(UserBase):
    password: str

# Schema para leitura de usuário (sem exibir senha)
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # <- atualização para Pydantic v2
