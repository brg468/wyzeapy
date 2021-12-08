from enum import Enum


class ResponseCodes(Enum):
    SUCCESS = "1"
    PARAMETER_ERROR = "1001"
    ACCESS_TOKEN_ERROR = "2001"
    DEVICE_OFFLINE = '3019'


class ResponseCodesLock(Enum):
    SUCCESS = 0
