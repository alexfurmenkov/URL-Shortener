"""
Response with status HTTP_200_OK
when everything is fine
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class ResponseSuccess(Response):
    """
    Response class
    """
    def __init__(self, message):
        super().__init__(status=HTTP_200_OK)
        self.data = dict(
            status='success',
            message=message,
        )
