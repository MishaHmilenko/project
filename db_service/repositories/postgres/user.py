from sqlalchemy.ext.asyncio import AsyncSession

from db.models.user import User
from grpc_db_service.user.dto import CreateUser
from interfaces.repositories.user_repository import IUserRepository
from repositories.postgres.base import BaseRepository


class UserRepository(IUserRepository, BaseRepository[User]):

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(model=User, session=session)

    async def create_user(self, user_data: CreateUser) -> None:
        user = self._model(
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            phone_number=user_data.phone_number,
            hashed_password=user_data.password
        )

        await self.save(user)

