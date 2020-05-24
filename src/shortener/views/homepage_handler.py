"""
Module with HomepageHandler class
to display the homepage
"""
from drf_yasg.utils import swagger_auto_schema

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class HomepageHandler(APIView):
    """
    Class-based view to handle requests on
    "/"
    """
    renderer_classes = [TemplateHTMLRenderer]

    @classmethod
    @swagger_auto_schema(
        responses={
            '200': 'Homepage Template is returned',
        }
    )
    def get(cls, request) -> Response:
        """
        Returns index.html page
        :param request: GET HTTP request
        :return: Response with rendered template
        """
        return Response(template_name='index.html')
