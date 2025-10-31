from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlmodel import Session, select
from typing import List
from fastapi.responses import HTMLResponse, JSONResponse

from app.database.connection import get_session
from app.models.favorite import Favorite
from app.schemas.favorite import FavoriteCreate, FavoriteResponse
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/favorites", tags=["Favorites"])


# ✅ Criar favorito (somente usuário logado)
@router.post("/", response_model=FavoriteResponse, status_code=status.HTTP_201_CREATED)
def create_favorite(
    fav: FavoriteCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    # Evitar duplicados
    exists_stmt = select(Favorite).where(
        (Favorite.movie_id == fav.movie_id) & (Favorite.user_id == current_user.id)
    )
    if session.exec(exists_stmt).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esse filme já está na sua lista de favoritos."
        )

    new = Favorite(**fav.dict(), user_id=current_user.id)
    try:
        session.add(new)
        session.commit()
        session.refresh(new)
        return new
    except Exception as ex:
        session.rollback()
        print("Erro ao criar favorito:", type(ex).__name__, ex)
        raise HTTPException(status_code=500, detail="Erro ao salvar favorito")


# ✅ Listar favoritos do usuário logado
@router.get("/", response_model=List[FavoriteResponse])
def list_favorites(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    stmt = select(Favorite).where(Favorite.user_id == current_user.id)
    favorites = session.exec(stmt).all()
    return favorites


# ✅ Deletar favorito (somente se for do usuário logado)
@router.delete("/{favorite_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_favorite(
    favorite_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    fav = session.get(Favorite, favorite_id)
    if not fav:
        raise HTTPException(status_code=404, detail="Favorito não encontrado.")

    if fav.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para deletar este favorito.")

    try:
        session.delete(fav)
        session.commit()
    except Exception as ex:
        session.rollback()
        print("Erro ao deletar favorito:", type(ex).__name__, ex)
        raise HTTPException(status_code=500, detail="Erro ao deletar favorito")

    return None


# ✅ Compartilhar favoritos (público)
@router.get("/share/{user_id}")
def share_favorites(
    user_id: int,
    request: Request,
    format: str = "json",
    session: Session = Depends(get_session)
):
    stmt = select(Favorite).where(Favorite.user_id == user_id)
    favorites = session.exec(stmt).all()

    if not favorites:
        msg = "<h2>Esse usuário ainda não tem filmes favoritos.</h2>"
        return HTMLResponse(msg, status_code=200)

    # JSON (para consumo por front-end)
    if format.lower() == "json":
        data = [FavoriteResponse.from_orm(fav).dict() for fav in favorites]
        return JSONResponse(content=data)

    # HTML (modo público)
    html_items = ""
    for fav in favorites:
        poster = fav.poster_path or "https://via.placeholder.com/250x370?text=Sem+Imagem"
        html_items += f"""
        <div style="border:1px solid #ccc; padding:10px; margin:10px; border-radius:10px; width:250px;">
            <img src="{poster}" alt="{fav.title}" style="width:100%; border-radius:10px;">
            <h3>{fav.title}</h3>
            <p>⭐ Nota: {fav.vote_average}</p>
            <p><b>ID do Filme:</b> {fav.movie_id}</p>
        </div>
        """

    html_content = f"""
    <html>
        <head>
            <title>Favoritos de Usuário {user_id}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    background-color: #f4f4f9;
                    padding: 20px;
                }}
                h1 {{
                    text-align: center;
                    width: 100%;
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <h1>Favoritos do Usuário {user_id}</h1>
            {html_items}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
