"""
Add view class or function to
__all__ to add it to the views module
"""
from .url_short_handler import UrlShortenHandler
from .resolve_short_url_handler import ResolveShortUrlHandler
from .homepage_handler import HomepageHandler


__all__ = [
    'UrlShortenHandler',
    'ResolveShortUrlHandler',
    'HomepageHandler',
]
