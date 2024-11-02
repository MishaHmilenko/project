from abc import ABC
from dataclasses import dataclass

from grpc_db_service.user.dto import CreateUser
from interfaces.repositories.base_repository import IRepository, Model


class IUserRepository(IRepository, ABC):

    async def create_user(self, model: CreateUser) -> Model:
        ...
