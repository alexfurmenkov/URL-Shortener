"""
Redis storage module to handle
operations with redis
"""
import json

import redis

from django.conf import settings


class RedisStorage(redis.StrictRedis):
    """
    Redis storage class
    """
    def __init__(self):
        super().__init__(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
        )

    def save_url_list(self, url_list, session_key):
        """
        Saves given list of urls
        to Redis key "url_list_<session_key>"
        :param url_list: List of urls
        :param session_key: Session key
        """
        for url in url_list:
            self.lpush(f'url_list_{session_key}', json.dumps(url))

    def append_url_to_list(self, url, session_key):
        """
        Appends new url to Redis
        key "url_list_<session_key>"
        :param url: Url to save in Redis
        :param session_key: Session key
        """
        return self.lpush(f'url_list_{session_key}', json.dumps(url))

    def remove_url_from_list(self, url, session_key):
        """
        Removes URL from url list
        :param url: URL to remove from list
        :param session_key: Session key
        """
        return self.lrem(
            name=f'url_list_{session_key}',
            count=0,
            value=json.dumps(url)
        )

    def get_url_list(self, session_key):
        """
        Returns list of all URLs of a current session key
        :param session_key: Session key
        :return: List with URLs of a current session key
        """
        url_list = self.lrange(f'url_list_{session_key}', 0, -1)
        if not url_list:
            return None

        url_list = [json.loads(url) for url in url_list]
        return url_list
