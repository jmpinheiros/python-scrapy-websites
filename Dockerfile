# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código-fonte para o diretório de trabalho
COPY . .

# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["scrapy", "crawl", "website", "-o", "/app/output/output.json"]


# Use a imagem oficial do Python como base
# FROM python:3.9-slim

# # Define o diretório de trabalho dentro do contêiner
# WORKDIR /app

# # Copia o arquivo de requisitos para o diretório de trabalho
# COPY requirements.txt .

# # Instala as dependências
# RUN pip install --no-cache-dir -r requirements.txt

# # Copia o resto do código-fonte para o diretório de trabalho
# COPY . .

# # Define o comando padrão a ser executado quando o contêiner for iniciado
# CMD ["./start.sh"]
