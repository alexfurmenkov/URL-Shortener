"""
Add middleware class or function to __all__
to add it to the middleware module
"""
from .save_session_middleware import SaveSessionMiddleware


__all__ = [
    'SaveSessionMiddleware',
]
