from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserByIDRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class BaseUserDataResponse(_message.Message):
    __slots__ = ("user_id", "email", "first_name", "last_name")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    email: str
    first_name: str
    last_name: str
    def __init__(self, user_id: _Optional[str] = ..., email: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class GetAllUsersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAllUsersResponse(_message.Message):
    __slots__ = ("users_data",)
    USERS_DATA_FIELD_NUMBER: _ClassVar[int]
    users_data: _containers.RepeatedCompositeFieldContainer[BaseUserDataResponse]
    def __init__(self, users_data: _Optional[_Iterable[_Union[BaseUserDataResponse, _Mapping]]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("email", "first_name", "last_name", "phone_number", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    first_name: str
    last_name: str
    phone_number: str
    password: str
    def __init__(self, email: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., phone_number: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class UpdateUserByIDRequest(_message.Message):
    __slots__ = ("user_id", "first_name", "last_name", "phone_number", "password")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    first_name: str
    last_name: str
    phone_number: str
    password: str
    def __init__(self, user_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., phone_number: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class DeleteUserByIDRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...
