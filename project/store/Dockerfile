FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install --no-cache-dir flask flask-sqlalchemy sqlalchemy

COPY . .

RUN chmod +x entrypoint.sh

EXPOSE 8888

ENTRYPOINT ["./entrypoint.sh"]
