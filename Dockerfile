FROM python:3.9-slim

# dentro do contêiner
WORKDIR /app

COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["scrapy", "crawl", "website", "-a", "urls_file=urls.txt", "-o", "/app/output/output.json"]
