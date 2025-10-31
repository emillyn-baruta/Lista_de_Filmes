import { useState } from "react";
import api from "../services/api";

function MovieSearch() {
  const [query, setQuery] = useState("");
  const [movies, setMovies] = useState([]);

  // Buscar filmes
  const handleSearch = async () => {
    if (!query) return;

    try {
      console.log("🔍 Buscando filmes com:", query);

      // ✅ Chama o backend (ajustar rota se necessário)
      const response = await api.get(`/movies/search/`, {
        params: { query },
      });

      console.log("🎬 Resposta da API:", response.data);
      setMovies(response.data.results || response.data || []);
    } catch (error) {
      console.error("❌ Erro ao buscar filmes:", error);
      alert("Erro ao buscar filmes. Verifique se o backend está rodando e a rota está correta.");
    }
  };

  // Salvar filme como favorito
  const salvarFavorito = async (movie) => {
    try {
      const response = await api.post("/favorites/", {
        movie_id: movie.id,
        title: movie.title,
        poster_path: movie.poster_path,
        vote_average: movie.vote_average,
      });

      if (response.status === 201) {
        alert(`"${movie.title}" foi adicionado aos favoritos!`);
      } else {
        alert("Não foi possível salvar o filme nos favoritos.");
      }
    } catch (error) {
      console.error("Erro ao salvar favorito:", error);
      alert("Erro ao salvar o favorito. Verifique se o backend está rodando.");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>🎬 Lista de Filmes</h1>
      <div>
        <input
          type="text"
          placeholder="Buscar filme..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{
            padding: "10px",
            width: "250px",
            marginRight: "10px",
            borderRadius: "8px",
            border: "1px solid #ccc",
          }}
        />
        <button
          onClick={handleSearch}
          style={{
            padding: "10px 20px",
            backgroundColor: "#1e90ff",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
          }}
        >
          Buscar
        </button>
      </div>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "center",
          marginTop: "20px",
        }}
      >
        {movies.map((movie) => (
          <div
            key={movie.id}
            style={{
              border: "1px solid #ccc",
              borderRadius: "10px",
              width: "200px",
              margin: "10px",
              padding: "10px",
              boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
            }}
          >
            <img
              src={movie.poster_path}
              alt={movie.title}
              style={{
                borderRadius: "10px",
                width: "100%",
                height: "300px",
                objectFit: "cover",
              }}
            />
            <h3 style={{ marginTop: "10px" }}>{movie.title}</h3>
            <p>⭐ {movie.vote_average}</p>
            <button
              onClick={() => salvarFavorito(movie)}
              style={{
                backgroundColor: "#ff4757",
                color: "white",
                border: "none",
                borderRadius: "8px",
                padding: "8px 12px",
                cursor: "pointer",
                marginTop: "8px",
              }}
            >
              Favoritar
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MovieSearch;
