from google.protobuf.json_format import MessageToDict

from grpc_db_service import db_service_pb2_grpc, db_service_pb2
from grpc_db_service.user.dto import CreateUser
from interfaces.repositories.user_repository import IUserRepository


class UserService(db_service_pb2_grpc.UserService):

    def __init__(self, repo: IUserRepository) -> None:
        self._repo = repo

    async def get_by_id(self, request: db_service_pb2.GetUserByIDRequest) -> db_service_pb2.BaseUserDataResponse:
        obj = await self._repo.get_by_id(id_=request.user_id)
        return db_service_pb2.BaseUserDataResponse(
            user_id=obj.id,
            email=obj.email,
            first_name=obj.first_name,
            last_name=obj.last_name,
        )

    async def get_all(self, request: db_service_pb2.GetAllUsersRequest) -> db_service_pb2.GetAllUsersResponse:
        users = await self._repo.get_all()

        response = db_service_pb2.GetAllUsersResponse()

        for user in users:

            response.users_data.append(
                db_service_pb2.BaseUserDataResponse(
                    user_id=user.id,
                    email=user.email,
                    first_name=user.first_name,
                    last_name=user.last_name,
                )
            )

        return response

    async def create(self, request: db_service_pb2.CreateUserRequest) -> None:

        user_dto = CreateUser(
            email=request.email,
            first_name=request.first_name,
            last_name=request.last_name,
            phone_number=request.password,
            password=request.password
        )
        await self._repo.create_user(user_dto)

    async def update(self, request: db_service_pb2.UpdateUserByIDRequest) -> None:
        update_fields = MessageToDict(
            request,
            preserving_proto_field_name=True,
        )

    async def delete(self, request: db_service_pb2.DeleteUserByIDRequest) -> None:
        user_id = request.user_id

        await self._repo.delete(user_id)
