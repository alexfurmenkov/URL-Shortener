"""
Add serializer class to __all__
to add it to the serializers module
"""
from .models import UrlAddressSerializer
from .validation import UrlShortenSerializer


__all__ = [
    'UrlAddressSerializer',
    'UrlShortenSerializer',
]
