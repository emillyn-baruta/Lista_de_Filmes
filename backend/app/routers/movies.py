# backend/app/routers/movies.py
from fastapi import APIRouter, HTTPException, Query
import requests
import os
from urllib.parse import quote

router = APIRouter(prefix="/movies", tags=["Filmes"])

# 🔑 Chave da API TMDb
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

@router.get("/search/")
def search_movies(query: str = Query(..., min_length=1)):
    """
    Busca filmes na API TMDb pelo nome digitado.
    Exemplo: /movies/search/?query=batman
    """
    if not TMDB_API_KEY:
        raise HTTPException(status_code=500, detail="TMDB_API_KEY não configurada no .env")

    # Codifica o termo de busca para evitar erro 400
    query_encoded = quote(query.strip())

    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=pt-BR&query={query_encoded}&include_adult=false"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        results = [
            {
                "id": movie.get("id"),
                "title": movie.get("title"),
                "overview": movie.get("overview"),
                "poster_path": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get("poster_path") else None,
                "vote_average": movie.get("vote_average"),
            }
            for movie in data.get("results", [])
            if movie.get("poster_path")  # evita filmes sem imagem
        ]

        return {"results": results}

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Tempo limite excedido ao consultar a TMDB")
    except requests.exceptions.RequestException as e:
        print("❌ Erro ao consultar TMDB:", e)
        raise HTTPException(status_code=502, detail="Erro ao conectar à API do TMDB")
    except Exception as e:
        print("❌ Erro inesperado:", e)
        raise HTTPException(status_code=500, detail="Erro interno ao buscar filmes")


@router.get("/{movie_id}")
def movie_details(movie_id: int):
    """
    Busca detalhes completos de um filme na API TMDb.
    Exemplo: /movies/550
    """
    if not TMDB_API_KEY:
        raise HTTPException(status_code=500, detail="TMDB_API_KEY não configurada no .env")

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=pt-BR"

    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 404:
            raise HTTPException(status_code=404, detail="Filme não encontrado na TMDB")
        resp.raise_for_status()

        data = resp.json()
        return {
            "id": data.get("id"),
            "title": data.get("title"),
            "overview": data.get("overview"),
            "poster_path": f"https://image.tmdb.org/t/p/w500{data.get('poster_path')}" if data.get("poster_path") else None,
            "vote_average": data.get("vote_average"),
            "genres": [g.get("name") for g in data.get("genres", [])],
            "release_date": data.get("release_date"),
            "runtime": data.get("runtime"),
        }

    except requests.exceptions.RequestException as e:
        print("❌ Erro ao buscar detalhes:", e)
        raise HTTPException(status_code=502, detail="Erro ao conectar à TMDB")
