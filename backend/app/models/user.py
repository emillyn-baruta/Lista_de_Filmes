from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
import secrets

if TYPE_CHECKING:
    from app.models.favorite import Favorite


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True, index=True, nullable=False)
    password: str

    # relacionamento: lista de favoritos
    favorites: List["Favorite"] = Relationship(back_populates="user")
