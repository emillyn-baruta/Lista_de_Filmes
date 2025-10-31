# backend/app/schemas/favorite.py
from pydantic import BaseModel
from typing import Optional

class FavoriteCreate(BaseModel):
    movie_id: int
    title: str
    poster_path: Optional[str] = None
    vote_average: Optional[float] = 0.0

class FavoriteResponse(FavoriteCreate):
    id: int

    class Config:
        from_attributes = True

