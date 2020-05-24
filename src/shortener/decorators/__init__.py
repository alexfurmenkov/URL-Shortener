"""
Add decorator to __all__ to add it
to the decorators module
"""
from .request_validation import request_validation

__all__ = [
    'request_validation',
]
