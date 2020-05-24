"""
Add redis class or function to
__all__ to add it to the utils.redis module
"""
from .redis_storage import RedisStorage


__all__ = [
    'RedisStorage',
]
