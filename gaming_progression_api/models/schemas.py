import datetime
import uuid

from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from gaming_progression_api.integrations.database import Base

from gaming_progression_api.models.users import  UserSchema


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=True)
    surname: Mapped[str] = mapped_column(nullable=True)
    patronymic: Mapped[str] = mapped_column(nullable=True)



    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
            surname=self.surname,
            patronymic=self.patronymic,
            email=self.email,
       
        )
