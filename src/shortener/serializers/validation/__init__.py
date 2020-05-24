"""
Add request validation serializer class
to __all__  to add it to the
serializers.validation module
"""
from .url_shorten_serializer import UrlShortenSerializer


__all__ = [
    'UrlShortenSerializer',
]
