"""
Add model serializer class to __all__
to add it to the serializers.models module
"""
from .url_address_serializer import UrlAddressSerializer


__all__ = [
    'UrlAddressSerializer',
]
