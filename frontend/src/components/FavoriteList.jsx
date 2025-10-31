import { useEffect, useState } from "react";
import axios from "axios";

function FavoriteList({ token }) {
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    const fetchFavorites = async () => {
      try {
        const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

        const response = await axios.get(`${API_URL}/favorites/`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        setFavorites(response.data);
      } catch (error) {
        console.error("Erro ao carregar favoritos:", error);
        if (error.response?.status === 401) {
          alert("Sessão expirada! Faça login novamente.");
          localStorage.removeItem("token");
          window.location.reload();
        }
      }
    };

    if (token) {
      fetchFavorites();
    }
  }, [token]);

  if (!token) {
    return <p>Faça login para ver seus favoritos.</p>;
  }

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>⭐ Meus Favoritos</h1>

      {favorites.length === 0 ? (
        <p>Nenhum favorito encontrado.</p>
      ) : (
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            justifyContent: "center",
            marginTop: "20px",
          }}
        >
          {favorites.map((fav) => (
            <div
              key={fav.id}
              style={{
                border: "1px solid #ccc",
                borderRadius: "10px",
                width: "200px",
                margin: "10px",
                padding: "10px",
              }}
            >
              <img
                src={fav.poster_path || "https://via.placeholder.com/200x300?text=Sem+Imagem"}
                alt={fav.title}
                style={{ width: "100%", borderRadius: "10px" }}
              />
              <h3>{fav.title}</h3>
              <p>⭐ {fav.vote_average}</p>
              <p>ID do Filme: {fav.movie_id}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default FavoriteList;
