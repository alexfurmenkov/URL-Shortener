"""
Serializer for UrlAddress model
"""
from rest_framework.serializers import ModelSerializer
from shortener.models import UrlAddress


class UrlAddressSerializer(ModelSerializer):
    """
    Serializer class
    """
    class Meta:
        model = UrlAddress
        fields = [
            'original_url',
            'short_url'
        ]
