from pydantic import BaseModel


class ResponseMessageSchema(BaseModel):
    """
    The ResponseMessage class.
    """

    message: str
