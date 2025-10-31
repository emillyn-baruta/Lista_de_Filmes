🎬 Lista de Filmes – Desafio Elite Dev (Verzel)

Aplicação Full Stack desenvolvida para o Desafio Elite Dev da Verzel, unindo FastAPI (Python) no back-end e React (Vite) no front-end.
O sistema permite pesquisar filmes pela API do TMDb, salvar favoritos e compartilhar listas personalizadas.

🧠 Stack Tecnológica
Categoria	Tecnologia
Frontend	React + Vite + Axios
Backend	FastAPI (Python 3.10+)
Banco de Dados	PostgreSQL
ORM	SQLModel
Integração Externa	TMDb API
Autenticação	Passlib (bcrypt)
Documentação	Swagger UI
Ambiente	dotenv
Deploy	Vercel (frontend) + Render/Railway (backend)
🚀 Funcionalidades
🔧 Backend (FastAPI)

CRUD de usuários e favoritos

Busca de filmes via TMDb API

Integração total com PostgreSQL

Rotas documentadas no Swagger UI

Senhas criptografadas com bcrypt

Compartilhamento de lista pública

💻 Frontend (React)

Busca dinâmica de filmes

Exibição de pôsteres e notas

Adicionar/remover favoritos

Visualizar lista de filmes salvos

Comunicação direta com o backend via Axios

🗂️ Estrutura de Pastas
desafio-elite-dev/
│
├── .venv/
│
├── backend/
│   └── app/
│       ├── __pycache__/
│       ├── main.py
│       │
│       ├── core/
│       │   ├── __pycache__/
│       │   └── security.py
│       │
│       ├── database/
│       │   ├── __pycache__/
│       │   ├── connection.py
│       │   └── database.db
│       │
│       ├── models/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   ├── favorite.py
│       │   └── user.py
│       │
│       ├── routers/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   ├── auth.py
│       │   ├── favorite_router.py
│       │   ├── movies.py
│       │   ├── user_router.py
│       │   └── main.py
│       │
│       └── schemas/
│           ├── __pycache__/
│           ├── __init__.py
│           ├── favorite.py
│           ├── main.py
│           └── user.py
│           └── user.py
│
│   ├── test_tmdb_speed.py
│   ├── requirements.txt
│
│
├── frontend/
│   ├── node_modules/
│   ├── public/
│   ├── vite.svg
│   │
│   ├── src/
│   │   ├── assets/
│   │   │   └── verzel_logo.svg
│   │   │
│   │   ├── components/
│   │   │   ├── AuthForms.css
│   │   │   ├── AuthForm.jsx
│   │   │   ├── FavoriteList.jsx
│   │   │   ├── Header.css
│   │   │   ├── Header.jsx
│   │   │   └── MovieSearch.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Favorites.css
│   │   │   ├── Favorites.jsx
│   │   │   ├── Login.css
│   │   │   └── Login.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── styles/
│   │   │   └── global.css
│   │   │
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── .env
│   ├── .eslintrc.config.js
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── README.md
│   ├── vite.config.js
│   └── .gitignore
│
├── .gitignore
└── README.md

⚙️ Como Rodar o Projeto Completo
🧩 1️⃣ Clonar o repositório
git clone https://github.com/emillyn-baruta/desafio-elite-dev.git
cd desafio-elite-dev

🗄️ 2️⃣ Rodar o Backend (FastAPI)

Entre na pasta do backend:

cd backend


Crie e ative o ambiente virtual:

python -m venv .venv
.venv\Scripts\activate  # Windows
# ou
source .venv/bin/activate  # Linux/Mac


Instale as dependências:

pip install -r requirements.txt


Configure o .env:

DATABASE_URL=postgresql+psycopg2://postgres:emi123@localhost:5432/postgres
TMDB_API_KEY=sua_chave_tmdb_aqui
SECRET_KEY=supersegredo_verzel_filmes_123
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60


Inicie o servidor:

uvicorn app.main:app --reload


✅ Acesse a API:

http://127.0.0.1:8000

Swagger: http://127.0.0.1:8000/docs

💻 3️⃣ Rodar o Frontend (React)

Entre na pasta do frontend:

cd ../frontend


Instale as dependências:

npm install


Crie o arquivo .env na pasta frontend/:

VITE_TMDB_API_KEY=sua_chave_tmdb_aqui
VITE_API_URL=http://127.0.0.1:8000


Inicie o servidor React:

npm run dev


✅ Acesse o site: http://localhost:5173

🔗 Integração Front–Back

O frontend consome a API via Axios, configurado em frontend/src/services/api.js:

import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export default api;

🧩 Principais Componentes do Frontend
🎞️ MovieCard.jsx

Exibe cada filme com:

Pôster

Título

Nota

Botão de Favoritar

🔍 SearchBar.jsx

Input controlado para buscar filmes pela API TMDb, com atualização em tempo real.

⭐ FavoritesList.jsx

Lista os filmes favoritos salvos no banco.

🌐 Rotas da Aplicação React
Caminho	Página	Descrição
/	Home	Busca de filmes
/favorites	Favoritos	Exibe lista salva
/share/:userId	Compartilhar	Exibe lista pública via backend
🧾 Endpoints do Backend
👤 Usuários

POST /users/ – Criar usuário

GET /users/ – Listar todos

🎬 Filmes

GET /movies/search/?query=matrix – Buscar filmes

GET /movies/{id} – Detalhes do filme

⭐ Favoritos

POST /favorites/ – Adicionar favorito

GET /favorites/user/{id} – Ver favoritos

DELETE /favorites/{id} – Remover favorito

📄 Banco de Dados (PostgreSQL)

Tabelas criadas automaticamente via SQLModel:

TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  password VARCHAR(200)
);

TABLE favorites (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200),
  movie_id INT,
  poster_path VARCHAR(300),
  vote_average FLOAT,
  user_id INT REFERENCES users(id)
);

☁️ Deploy
Serviço	Uso	Link 


Vercel	Frontend (React)	https://lista-filmes-omega.vercel.app/


👩‍💻 Autora

Emillyn Baruta Machado
💻 Desenvolvedora Full Stack Python | React
📍 Curitiba – PR
🔗 (https://www.linkedin.com/in/emillyn-baruta-machado-/)
🔗 GitHub: https://github.com/emillyn-baruta
