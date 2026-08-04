# Imagem base enxuta, adequada para aplicações Python em produção
FROM python:3.12-slim

# Evita a geração de arquivos .pyc e garante logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copia e instala dependências antes do código-fonte para
# aproveitar o cache de camadas do Docker em builds futuros
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY app/ ./app/

# Usuário não-root por questões de segurança
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.app:app"]
