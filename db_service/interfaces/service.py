from abc import ABC, abstractmethod


class IService(ABC):

    @abstractmethod
    async def get_by_id(self, id_: str):
        ...

    @abstractmethod
    async def get_all(self):
        ...

    @abstractmethod
    async def create(self, *kwargs) -> None:
        ...