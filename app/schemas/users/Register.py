import re
from typing import Annotated, Literal

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, field_validator
from pydantic_core import PydanticCustomError


class RequestRegisterUser(BaseModel):
    class Config:
        from_attributes = True

    username: Annotated[str, MinLen(3), MaxLen(20)]
    password: str
    gender: Literal['male', 'female']
    birthday: str
    last_name: Annotated[str, MinLen(2), MaxLen(20)]
    first_name: Annotated[str, MinLen(2), MaxLen(20)]
    email: EmailStr | None = None

    @field_validator('password')
    def valid_pass(cls, v):
        regex = r"^[a-zA-Z0-9]{8,16}$"

        if bool(re.match(regex, v)):
            return v

        if v != 'password':
            raise PydanticCustomError(
                f"{regex}",
                'value is not valid "{wrong_value}"',
                dict(wrong_value=v),
            )

        return v

    @field_validator('birthday')
    def valid_birthday(cls, v):
        regex = r"^(19|20)[0-9]{2}-(0[1-9]|1[0-2])-(0[1-9]|[1-3][0-1])$"

        if bool(re.match(regex, v)):
            return v

        if v != 'birthday':
            raise PydanticCustomError(
                f"{regex}",
                'value is not valid "{wrong_value}"',
                dict(wrong_value=v),
            )

        return v


class ResponseRegisterUser(BaseModel):
    username: str
    email: str | None
    message: str
