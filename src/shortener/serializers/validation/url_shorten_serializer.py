"""
Serializer for POST HTTP request
on URL "api/shorten/"
"""
from rest_framework.serializers import (
    Serializer,
    CharField
)


class UrlShortenSerializer(Serializer):
    """
    Serializer class
    """
    original_url = CharField(required=True, label='original_url',
                             max_length=8192)
    short_url = CharField(required=False, label='short_url',
                          max_length=8192)
