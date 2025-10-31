// frontend/src/pages/Login.jsx
import { useState } from "react";
import api from "../services/api";
import "./Login.css";
import verzelLogo from "../assets/verzel logo.svg";

export default function Login({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const response = await api.post("/auth/login", { email, password });
      console.log("Resposta do backend:", response.data);

      // Captura o token JWT retornado pelo backend
      const token = response.data?.access_token;

      if (token && typeof token === "string") {
        localStorage.setItem("token", token);
        console.log("Token salvo no localStorage:", token);

        alert("✅ Login realizado com sucesso!");
        onLogin(token);
      } else {
        console.error("Token não recebido ou inválido:", response.data);
        setError("Erro ao processar a resposta do servidor.");
      }
    } catch (err) {
      console.error("Erro no login:", err);
      setError(err.response?.data?.detail || "Email ou senha incorretos.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-container fade-in">
      <div className="logo-header">
        <img src={verzelLogo} alt="Logo Verzel" className="logo-verzel" />
        <h2>VERZEL FILMES</h2>
      </div>

      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Senha"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          autoComplete="current-password"
        />

        <button type="submit" disabled={loading}>
          {loading ? "Entrando..." : "Entrar"}
        </button>
      </form>

      {error && <p className="error">{error}</p>}
    </div>
  );
}
