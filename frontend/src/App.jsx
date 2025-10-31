// frontend/src/App.jsx
import { useState, useEffect } from "react";
import MovieSearch from "./components/MovieSearch";
import FavoriteList from "./components/FavoriteList";
import Favorites from "./pages/Favorites";
import Header from "./components/Header";
import AuthForm from "./components/AuthForm";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || "");
  const [currentPage, setCurrentPage] = useState("home");

  // Garante que o token no estado sempre acompanha o localStorage
  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    if (storedToken && storedToken !== token) {
      setToken(storedToken);
    }
  }, []);

  const handleLogin = (newToken) => {
    localStorage.setItem("token", newToken);
    setToken(newToken);
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken("");
    setCurrentPage("home");
  };

  // 🔒 Se não houver token, mostra o AuthForm (login/cadastro)
  if (!token) {
    return <AuthForm onLogin={handleLogin} />;
  }

  return (
    <div className="app-container">
      <Header token={token} onLogout={handleLogout} />

      <div style={{ padding: "20px", fontFamily: "Poppins, sans-serif" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
         

          <div>
            {currentPage === "home" ? (
              <button
                onClick={() => setCurrentPage("favorites")}
                style={{
                  background: "#007bff",
                  color: "white",
                  border: "none",
                  padding: "6px 12px",
                  borderRadius: "6px",
                  marginRight: "10px",
                  cursor: "pointer",
                }}
              >
                Meus Favoritos ⭐
              </button>
            ) : (
              <button
                onClick={() => setCurrentPage("home")}
                style={{
                  background: "#007bff",
                  color: "white",
                  border: "none",
                  padding: "6px 12px",
                  borderRadius: "6px",
                  marginRight: "10px",
                  cursor: "pointer",
                }}
              >
                Voltar à Lista 🎬
              </button>
            )}

            <button
              onClick={handleLogout}
              style={{
                background: "red",
                color: "white",
                border: "none",
                padding: "6px 12px",
                cursor: "pointer",
                borderRadius: "6px",
              }}
            >
              Logout
            </button>
          </div>
        </div>

        <hr />

        {currentPage === "home" ? (
          <>
            <MovieSearch token={token} />
            <hr />
            <FavoriteList token={token} />
          </>
        ) : (
          <Favorites />
        )}
      </div>
    </div>
  );
}

export default App;
