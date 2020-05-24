"""
Middleware to save session on every request
"""


class SaveSessionMiddleware:
    """
    Middleware class
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Saves session on every request
        if it doesn't exist
        :param request: Any HTTP request
        :return: Passes the request further with saved session
        """
        if not request.session.session_key:
            request.session.save()

        response = self.get_response(request)
        return response
