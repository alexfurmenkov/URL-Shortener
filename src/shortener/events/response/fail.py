"""
Response with status HTTP_400_BAD_REQUEST
when something is wrong
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class ResponseFail(Response):
    """
    Response class
    """
    def __init__(self, message):
        super().__init__(status=HTTP_400_BAD_REQUEST)
        self.data = dict(
            status='fail',
            message=message,
        )
