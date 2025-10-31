from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User


class Favorite(SQLModel, table=True):
    __tablename__ = "favorites"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    movie_id: int
    poster_path: Optional[str] = None
    vote_average: Optional[float] = 0.0
    user_id: int = Field(foreign_key="users.id")

    user: Optional["User"] = Relationship(back_populates="favorites")
