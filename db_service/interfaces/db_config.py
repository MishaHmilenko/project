from abc import ABC, abstractmethod


class DBConfigStrategy(ABC):

    @abstractmethod
    def get_url(self) -> str:
        ...