// frontend/src/components/AuthForm.jsx
import React, { useState } from "react";
import api from "../services/api";
import "./AuthForm.css";
import verzelLogo from "../assets/verzel logo.svg";

export default function AuthForm({ onLogin }) {
  const [isRegister, setIsRegister] = useState(false);
  const [formData, setFormData] = useState({ name: "", email: "", password: "" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      if (isRegister) {
        await api.post("/auth/register", formData);
        alert("✅ Cadastro realizado! Agora faça login.");
        setIsRegister(false);
      } else {
        const response = await api.post("/auth/login", {
          email: formData.email,
          password: formData.password,
        });

        const token = response.data?.access_token;
        if (token) {
          localStorage.setItem("token", token);
          onLogin(token);
        } else {
          setError("Token inválido recebido do servidor.");
        }
      }
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.detail || "Erro ao processar solicitação.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <img src={verzelLogo} alt="Verzel logo" className="auth-logo-large" />
      <h1 className="auth-title-main">Filmes</h1>

      <form className="auth-form" onSubmit={handleSubmit}>
        {isRegister && (
          <input
            type="text"
            name="name"
            placeholder="Nome"
            value={formData.name}
            onChange={handleChange}
            required
          />
        )}
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Senha"
          value={formData.password}
          onChange={handleChange}
          required
        />

        <button type="submit" className="auth-button" disabled={loading}>
          {loading ? "Carregando..." : isRegister ? "Cadastrar" : "Entrar"}
        </button>
      </form>

      {error && <p className="error">{error}</p>}

      <div className="auth-footer">
        {isRegister ? (
          <p>
            Já tem uma conta? <span onClick={() => setIsRegister(false)}>Entrar</span>
          </p>
        ) : (
          <p>
            Novo por aqui? <span onClick={() => setIsRegister(true)}>Criar conta</span>
          </p>
        )}
      </div>
    </div>
  );
}
