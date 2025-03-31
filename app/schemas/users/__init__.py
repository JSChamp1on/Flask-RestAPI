from .Get import (
    RequestGetUser,
    ResponseGetUser,
    ResponseUserList,
)
from .Login import (
    RequestLoginUser,
    ResponseLoginUser,
)
from .Register import (
    RequestRegisterUser,
    ResponseRegisterUser,
)


requestGetUser = RequestGetUser()
responseGetUser = ResponseGetUser()
responseUserList = ResponseUserList()
requestLoginUser = RequestLoginUser()
responseLoginUser = ResponseLoginUser()
requestRegisterUser = RequestRegisterUser()
responseRegisterUser = ResponseRegisterUser()
