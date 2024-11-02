from typing import Generic

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.repositories.base_repository import Model, IRepository


class BaseRepository(IRepository, Generic[Model]):

    def __init__(self, model: type[Model], session: AsyncSession) -> None:
        self._model = model
        self._session = session

    async def get_by_id(self, id_: str) -> Model:
        query = select(self._model).where(self._model.id == id_)
        return (await self._session.execute(query)).scalar_one()

    async def get_all(self) -> list[Model]:
        query = select(self._model)
        return (await self._session.execute(query)).scalars.all()

    async def update_obj(self, id_: str, **kwargs) -> None:
        query = update(self._model).where(self._model.id == id_).values(kwargs)
        await self._session.execute(query)

    async def delete(self, id_: str) -> None:
        query = delete().where(self._model.id == id_)
        await self._session.execute(query)

    async def save(self, obj: Model) -> None:
        self._session.add(obj)
