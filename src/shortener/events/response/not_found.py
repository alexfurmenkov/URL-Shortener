"""
Response with status HTTP_404_NOT_FOUND
when resource is not found
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND


class ResponseNotFound(Response):
    """
    Response class
    """
    def __init__(self, message: str):
        super().__init__(status=HTTP_404_NOT_FOUND)
        self.data = dict(
            status='fail',
            message=message,
        )
