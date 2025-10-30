# 🎬 Lista de Filmes  

Aplicação Full Stack desenvolvida para o **Desafio Elite Dev (Verzel)**.  
Permite ao usuário **pesquisar filmes pela API do TMDb** e **salvar seus favoritos** em uma lista pessoal.  
O backend foi construído em **Python (FastAPI)** com **PostgreSQL + SQLModel**, seguindo boas práticas de arquitetura, segurança e documentação interativa via **Swagger**.

---

## 🚀 Funcionalidades Principais
- 🔍 Buscar filmes pela API do **TMDb**  
- 👤 Criar e listar **usuários**  
- ⭐ Adicionar ou remover **filmes favoritos**  
- 🌐 Gerar uma **página pública** com os favoritos de cada usuário (HTML ou JSON)

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
| Deploy Opcional | **Render**, **Vercel (frontend)** ou **Railway** |

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



---

## ⚙️ Configuração do Ambiente

### 1️⃣ Pré-requisitos
- Python 3.10+
- PostgreSQL instalado e em execução
- Chave de API válida do [The Movie Database (TMDb)](https://developer.themoviedb.org/)

---

### 2️⃣ Clonar o repositório


git clone https://github.com/emillyn-baruta/Lista_de_Filmes
cd desafio-elite-dev/backend
3️⃣ Criar e ativar ambiente virtual

python -m venv venv
venv\Scripts\activate     # Windows
# ou
source venv/bin/activate  # Linux/Mac
4️⃣ Instalar dependências

pip install -r requirements.txt
5️⃣ Configurar o arquivo .env
Na raiz do projeto (backend/), crie um arquivo chamado .env com o seguinte conteúdo:

DATABASE_URL=postgresql+psycopg2://postgres:SENHA@localhost:5432/NOMEDOBANCO
TMDB_API_KEY=sua_chave_tmdb_aqui
💡 Nota: Caso tenha dúvidas sobre onde encontrar sua senha do PostgreSQL ou gerar a TMDB API Key, veja a seção 📄 Detalhes sobre o .env.

6️⃣ Rodar a aplicação

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

{
  "movie_id": 603692,
  "title": "John Wick 4",
  "poster_path": "https://image.tmdb.org/t/p/w500/abc123.jpg",
  "vote_average": 8.9,
  "user_id": 1
}
🧩 Visão Técnica
A aplicação foi construída com foco em modularidade e boas práticas:

Camadas separadas: routers, models, schemas e conexão de banco isoladas.

ORM tipado (SQLModel): garante integridade e produtividade.

Senhas criptografadas com bcrypt.

Tratamento de exceções e rollback em transações críticas.

Integração externa com TMDb API via requests assíncronos.

CORS configurado para integração futura com frontend React.

🛠️ Banco de Dados
Tabelas geradas automaticamente no PostgreSQL:

users

id, name, email, password (bcrypt hash)

favorites

id, title, movie_id, poster_path, vote_average, user_id (FK → users)

A criação é feita automaticamente na inicialização do app (on_startup em main.py).

💡 Decisões Técnicas
FastAPI + SQLModel: escolhido pela produtividade e tipagem forte, além de integração nativa com Swagger.

Arquitetura modular com divisão clara entre camadas.

Senhas criptografadas com bcrypt.

CORS configurado para integração com o frontend React.

Tratamento de exceções e mensagens HTTP padronizadas.

Rota /favorites/share permite visualização pública (HTML/JSON).

🧩 Melhorias Futuras
🔐 Implementar autenticação JWT.

🧪 Adicionar testes automatizados (Pytest).

💻 Criar frontend em React + Vite integrado à API.

☁️ Deploy completo no Render/Railway com documentação pública.

☁️ Deploy (Opcional +1 ponto)
Para o desafio, é possível:

Hospedar o backend no Render ou Railway.

Deploy do frontend (quando pronto) na Vercel.

📄 Detalhes sobre o .env
🔐 Sobre a senha do PostgreSQL
Quando você instalou o PostgreSQL, o instalador pediu uma senha para o usuário postgres.
Essa é a senha usada no .env.
Se esqueceu, você pode redefinir via pgAdmin → Login/Group Roles → postgres → Properties → Definition → Password.

Exemplo:

bash
Copiar código
DATABASE_URL=postgresql+psycopg2://postgres:minhasenha123@localhost:5432/filmesdb
🎬 Sobre a chave TMDb
Crie sua conta em https://www.themoviedb.org/
→ Vá em Configurações → API → Create API Key (Developer).
A TMDb gerará uma chave como esta:
TMDB_API_KEY=ab1234cdef56789ghijklm


👩‍💻 Autora
Emillyn Baruta Machado
💼 Desenvolvedora Full Stack Python | React
🔗 LinkedIn • GitHub
