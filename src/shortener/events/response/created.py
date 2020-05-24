"""
Response with status HTTP_201_CREATED
when created a new resource
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class ResponseCreated(Response):
    """
    Response class
    """
    def __init__(self, message):
        super().__init__(status=HTTP_201_CREATED)
        self.data = dict(
            status='success',
            message=message,
        )
