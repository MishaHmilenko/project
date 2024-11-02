import uuid

from sqlalchemy import String, types
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import Base


class User(Base):

    __tablename__ = 'User'

    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))

    email: Mapped[str] = mapped_column(unique=True, nullable=False)

    phone_number: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)

    hashed_password: Mapped[str] = mapped_column(nullable=False)
