import contextlib
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncConnection

from interfaces.db_connection import IDatabaseManager

from db.models.user import Base

from db.config import PostgresDBConfig, DBConfig


class PostgresManager(IDatabaseManager):

    def __init__(self, config: DBConfig) -> None:
        self._engine = create_async_engine(url=config.get_url, echo=True)
        self._sessionmaker = async_sessionmaker(bind=self._engine, autocommit=False)

    async def close(self) -> None:

        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        await self._engine.dispose()

        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:

        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self._engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncIterator]:

        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


sessionmanager: IDatabaseManager = PostgresManager(config=DBConfig(db_strategy=PostgresDBConfig()))


async def get_db_session():
    async with sessionmanager.session() as session:
        yield session
