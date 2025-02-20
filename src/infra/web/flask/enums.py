from enum import Enum


class HttpMethods(str, Enum):
    """
    Http Methods allowed
    """

    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"


class HttpStatusCodes(int, Enum):
    """
    Http Status Codes
    """

    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
