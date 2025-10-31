// src/components/Header.jsx
import React from "react";
import logo from "../assets/verzel logo.svg";
import "./Header.css"; // 👈 criaremos já

export default function Header({ token, onLogout }) {
  return (
    <header className="header app-container" role="banner">
      <div className="brand">
        <img src={logo} alt="Verzel logo" className="logo" />
        <div>
          <h1 className="title">VERZEL <span>Filmes</span></h1>
          <p className="subtitle">Seu catálogo pessoal</p>
        </div>
      </div>

      <div className="header-right">
        {token ? (
          <>
            <button className="btn ghost" onClick={() => window.location.reload()}>
              Minha Conta
            </button>
            <button className="btn logout" onClick={onLogout}>Logout</button>
          </>
        ) : (
          <p className="welcome">Bem-vindo</p>
        )}
      </div>
    </header>
  );
}
