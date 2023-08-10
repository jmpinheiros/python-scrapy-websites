FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código-fonte para o diretório de trabalho
COPY . .
