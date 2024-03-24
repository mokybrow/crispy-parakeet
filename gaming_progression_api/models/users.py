import datetime

from pydantic import UUID4, BaseModel, ConfigDict, EmailStr


class UserSchema(BaseModel):
    id: UUID4
    email: str
    name: str
    surname: str
    patronymic: str
    model_config = ConfigDict(arbitrary_types_allowed=True)

