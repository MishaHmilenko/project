from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from db.models.base import Base

Model = TypeVar('Model', bound=Base)


class IRepository(ABC, Generic[Model]):

    @abstractmethod
    async def get_by_id(self, id_: str) -> Model:
        ...

    @abstractmethod
    async def get_all(self) -> list[Model]:
        ...

    @abstractmethod
    async def update_obj(self, id_: str, **kwargs) -> None:
        ...

    @abstractmethod
    async def delete(self, id_: str) -> None:
        ...

    @abstractmethod
    async def save(self, obj: Model) -> None:
        ...
