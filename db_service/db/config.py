import os

from interfaces.db_config import DBConfigStrategy


class PostgresDBConfig(DBConfigStrategy):
    user: str = os.getenv('DB_USER')
    password: str = os.getenv('DB_PASSWORD')
    database: str = os.getenv('DB_NAME')
    host: str = os.getenv('DB_HOST')
    port: int = os.getenv('DB_PORT', 5432)

    def get_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class DBConfig:

    def __init__(self, db_strategy: DBConfigStrategy) -> None:
        self.db_strategy = db_strategy

    @property
    def get_url(self) -> str:
        return self.db_strategy.get_url()
