# Lista_de_Filmes
Repositório para que o usuário possa pesquisar pesquisar filmes e salvar uma lista de favoritos, conecta com o TMDb.
Aplicação desenvolvida em Python (FastAPI) com PostgreSQL e SQLModel, que permite ao usuário pesquisar filmes e salvar seus favoritos em uma lista pessoal.
O projeto foi estruturado com foco em boas práticas de desenvolvimento Full Stack, seguindo padrões de organização, rotas bem definidas e persistência de dados.
# 🎬 Desafio Elite Dev — Verzel

API desenvolvida para o **Desafio Elite Dev (Verzel)**, com o objetivo de validar conhecimentos Full Stack em **FastAPI (Python)**, **PostgreSQL** e integração com a **API do The Movie Database (TMDb)**.  
O backend foi implementado seguindo boas práticas de arquitetura, segurança e documentação interativa via Swagger.

---

## 🚀 Visão Geral

A aplicação é uma **Lista de Filmes** que permite:

- Buscar filmes pela API do **TMDb**.  
- Criar e listar **usuários**.  
- Adicionar ou remover **filmes favoritos** de um usuário.  
- Gerar uma **página compartilhável com os favoritos** de cada usuário (HTML ou JSON).  

Toda a persistência é feita com **PostgreSQL**, utilizando **SQLModel** como ORM.

---

## 🧠 Stack Tecnológica

| Categoria | Tecnologia |
|------------|-------------|
| Backend | **FastAPI** |
| ORM | **SQLModel** |
| Banco de Dados | **PostgreSQL** |
| Integração Externa | **TMDb API** |
| Autenticação de Senha | **Passlib (bcrypt)** |
| Variáveis de Ambiente | **python-dotenv** |
| Testes via Interface | **Swagger UI (/docs)** |
| Deploy Opcional | **Render**, **Vercel (via frontend)** ou **Railway** |

---

## 🗂️ Estrutura de Pastas

backend/
│
├── app/
│ ├── main.py # Ponto de entrada do servidor FastAPI
│ ├── database/
│ │ ├── connection.py # Conexão e criação das tabelas no PostgreSQL
│ │ └── database.db
│ ├── models/ # Modelos SQLModel (tabelas)
│ │ ├── user.py
│ │ └── favorite.py
│ ├── routers/ # Rotas da API (divididas por contexto)
│ │ ├── user_router.py
│ │ ├── favorite_router.py
│ │ └── movies.py
│ ├── schemas/ # Schemas Pydantic (validação e resposta)
│ │ ├── user.py
│ │ └── favorite.py
│ └── init.py
│
├── .env # Configurações sensíveis (chaves e banco)
├── requirements.txt # Dependências do projeto
└── README.md

yaml
Copiar código

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Pré-requisitos
- Python 3.10+
- PostgreSQL instalado e em execução
- Chave de API válida do [The Movie Database (TMDb)](https://developer.themoviedb.org/)

---

### 2️⃣ Clonar o repositório

```bash
git clone https://github.com/emillyn-dev/desafio-elite-dev.git
cd desafio-elite-dev/backend
3️⃣ Criar e ativar ambiente virtual
bash
Copiar código
python -m venv venv
venv\Scripts\activate     # Windows
# ou
source venv/bin/activate  # Linux/Mac
4️⃣ Instalar dependências
bash
Copiar código
pip install -r requirements.txt
5️⃣ Configurar o arquivo .env
Na raiz do projeto (backend/), crie um arquivo .env com o seguinte conteúdo:

bash
Copiar código
DATABASE_URL=postgresql+psycopg2://postgres:SENHA@localhost:5432/NOMEDOBANCO
TMDB_API_KEY=sua_chave_tmdb_aqui
6️⃣ Rodar a aplicação
bash
Copiar código
uvicorn app.main:app --reload
O servidor será iniciado em:
👉 http://127.0.0.1:8000

Documentação interativa (Swagger):
👉 http://127.0.0.1:8000/docs

🧩 Endpoints Principais
👤 Usuários (/users)
Método	Endpoint	Descrição
GET	/users/	Lista todos os usuários cadastrados
POST	/users/	Cria um novo usuário com senha criptografada

Exemplo de criação

json
Copiar código
{
  "name": "Emillyn Dev",
  "email": "emillyn@example.com",
  "password": "123456"
}
🎞️ Filmes (/movies)
Método	Endpoint	Descrição
GET	/movies/search/?query=batman	Busca filmes pelo nome via TMDb
GET	/movies/{movie_id}	Retorna detalhes completos de um filme

⭐ Favoritos (/favorites)
Método	Endpoint	Descrição
POST	/favorites/	Adiciona um filme aos favoritos de um usuário
GET	/favorites/user/{user_id}	Lista os favoritos de um usuário
DELETE	/favorites/{favorite_id}	Remove um favorito
GET	/favorites/share/{user_id}?format=html	Gera uma página pública com os favoritos

Exemplo de criação

json
Copiar código
{
  "movie_id": 603692,
  "title": "John Wick 4",
  "poster_path": "https://image.tmdb.org/t/p/w500/abc123.jpg",
  "vote_average": 8.9,
  "user_id": 1
}
🛠️ Banco de Dados
Tabelas geradas automaticamente no PostgreSQL:

users

id, name, email, password (bcrypt hash)

favorites

id, title, movie_id, poster_path, vote_average, user_id (FK → users)

A criação é feita automaticamente na inicialização do app (on_startup em main.py).

💡 Decisões Técnicas
FastAPI + SQLModel: escolhido pela produtividade e tipagem forte, além de integração nativa com Swagger.

Arquitetura modular com divisão clara entre routers, models, schemas e database.

Senhas criptografadas com bcrypt.

Tratamento de exceções com rollback e mensagens HTTP padronizadas.

CORS configurado para permitir integração com o frontend React.

Rota /favorites/share permite visualização pública (HTML) e API (JSON).

🧩 Melhorias Futuras
Implementar autenticação JWT.

Adicionar testes automatizados (Pytest).

Criar frontend em React + Vite integrado a esta API.

Fazer deploy completo (Render ou Railway) com documentação pública.

☁️ Deploy (opcional +1 ponto)
Para ganhar o ponto extra do desafio, é possível:

Hospedar o backend no Render ou Railway.

Deploy do frontend (quando pronto) na Vercel.

👩‍💻 Autora
Emillyn Dev
💼 Desenvolvedora Full Stack Python | React
📧 emillyn@example.com
🌐 GitHub: github.com/emillyn-dev
