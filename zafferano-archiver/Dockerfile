FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip\
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY scraper.py .
COPY app.py .
COPY bin/* ./bin/
RUN chmod +x ./bin/*
RUN ln -s /app/bin/zpull.sh /bin/zpull

CMD ["python", "app.py"]
