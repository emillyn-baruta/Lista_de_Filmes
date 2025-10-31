import { useEffect, useState } from "react";
import api from "../services/api";
import "./Favorites.css";

export default function Favorites() {
  const [favorites, setFavorites] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchFavorites = async () => {
      try {
        const token = localStorage.getItem("token");
        if (!token) {
          alert("Você precisa estar logado para ver seus favoritos!");
          return;
        }

        const response = await api.get("/favorites", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        setFavorites(response.data);
      } catch (err) {
        console.error("Erro ao buscar favoritos:", err);
        alert("Erro ao carregar seus favoritos.");
      } finally {
        setLoading(false);
      }
    };

    fetchFavorites();
  }, []);

  const handleRemove = async (id) => {
    const confirmar = confirm("Tem certeza que deseja remover este favorito?");
    if (!confirmar) return;

    try {
      const token = localStorage.getItem("token");
      await api.delete(`/favorites/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setFavorites(favorites.filter((fav) => fav.id !== id));
      alert("Filme removido dos favoritos!");
    } catch (err) {
      console.error("Erro ao remover favorito:", err);
      alert("Erro ao remover o favorito.");
    }
  };

  if (loading) {
    return <p>Carregando favoritos...</p>;
  }

  return (
    <div className="favorites-container">
      <h2>🎬 Meus Favoritos</h2>

      {favorites.length === 0 ? (
        <p>Você ainda não tem filmes favoritos.</p>
      ) : (
        <div className="favorites-grid">
          {favorites.map((fav) => (
            <div key={fav.id} className="favorite-card">
              <img
                src={
                  fav.poster_path ||
                  "https://via.placeholder.com/250x370?text=Sem+Imagem"
                }
                alt={fav.title}
              />
              <h3>{fav.title}</h3>
              <p>⭐ {fav.vote_average}</p>
              <button onClick={() => handleRemove(fav.id)}>Remover</button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
