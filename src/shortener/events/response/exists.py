"""
Response with status HTTP_409_CONFLICT
when the resource that user is trying
to create already exists
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_409_CONFLICT


class ResponseAlreadyExists(Response):
    """
    Response class
    """
    def __init__(self, message):
        super().__init__(status=HTTP_409_CONFLICT)
        self.data = dict(
            status='fail',
            message=message,
        )
