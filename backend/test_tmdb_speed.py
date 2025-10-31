import requests
import time
import os
from dotenv import load_dotenv

# Carrega o arquivo .env (ajuste o caminho se precisar)
load_dotenv(r"C:\Users\Dell\desafio-elite-dev\backend\.env")

TMDB_TOKEN = os.getenv("TMDB_READ_ACCESS_TOKEN")

url = "https://api.themoviedb.org/3/search/movie"
params = {
    "language": "pt-BR",
    "query": "homem",
}

headers = {
    "Authorization": f"Bearer {TMDB_TOKEN}",
    "Content-Type": "application/json;charset=utf-8",
}

print("🔍 Testando velocidade da API TMDb...")
start = time.time()
try:
    response = requests.get(url, headers=headers, params=params, timeout=10)
    print(f"Status code: {response.status_code}")
    print(f"Tempo de resposta: {time.time() - start:.2f} segundos")

    if response.status_code == 200:
        data = response.json()
        print(f"✅ Sucesso! Foram encontrados {len(data.get('results', []))} filmes.")
    else:
        print(f"❌ Erro na API: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"❌ Erro: {e}")
