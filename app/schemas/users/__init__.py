from .Get import (
    RequestGetUser,
    ResponseGetUser,
    ResponseUserList,
)
from .Login import (
    RequestLoginUser,
    ResponseLoginUser,
    ResponseUserStatus,
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
responseUserStatus = ResponseUserStatus()
requestRegisterUser = RequestRegisterUser()
responseRegisterUser = ResponseRegisterUser()
