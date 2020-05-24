"""
Decorator to validate request parameters
according to the given serializer
"""
import functools

from shortener.events import ResponseFail


def request_validation(serializer):
    """
    Validates request according to the given serializer
    :param serializer: HTTP Request serializer
    :return: Passes the request further if the serializer is valid
    """
    def _decorator(handler):
        @functools.wraps(handler)
        def _wrapper(view, request, *args, **kwargs):
            if request.method == 'GET':
                serialized_data = serializer(data=request.query_params)
            else:
                serialized_data = serializer(data=request.data)
            if not serialized_data.is_valid():
                return ResponseFail(serialized_data.errors)
            return handler(view, request, *args, **kwargs)

        return _wrapper

    return _decorator
