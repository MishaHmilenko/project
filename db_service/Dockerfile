FROM python:3.11-slim

WORKDIR app/

COPY ../poetry.lock ../pyproject.toml /app/

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --with db-service

COPY ./db_service /app/

CMD alembic upgrade head && python main.py
