import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // 👈 use sempre o mesmo IP do backend
  headers: {
    "Content-Type": "application/json",
  },
});

// Intercepta requisições e adiciona o token JWT se existir
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
