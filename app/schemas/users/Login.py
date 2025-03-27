from pydantic import BaseModel


class RequestLoginUser(BaseModel):
    class Config:
        from_attributes = True

    username: str
    password: str


class ResponseLoginUser(BaseModel):
    username: str
    message: str
