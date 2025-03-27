from typing import List

from pydantic import BaseModel


class RequestGetUser(BaseModel):
    class Config:
        from_attributes = True

    username: str | None = None


class ResponseGetUser(BaseModel):
    username: str | None


class ResponseFullGetUser(BaseModel):
    username: str
    gender: str
    birthday: str
    last_name: str
    first_name: str


class ResponseUserList(BaseModel):
    users: List[ResponseGetUser] | List[ResponseFullGetUser]
