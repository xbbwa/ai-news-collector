FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY collector ./collector
COPY config ./config
COPY scripts ./scripts

RUN mkdir -p /app/data
VOLUME ["/app/data"]

CMD ["python", "-m", "collector", "run"]
