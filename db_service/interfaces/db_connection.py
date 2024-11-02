from abc import ABC, abstractmethod
from typing import AsyncIterator, Any


class IDatabaseManager(ABC):

    @abstractmethod
    def close(self) -> None:
        ...

    @abstractmethod
    def connect(self) -> AsyncIterator[Any]:
        ...

    @abstractmethod
    def session(self) -> AsyncIterator[Any]:
        ...