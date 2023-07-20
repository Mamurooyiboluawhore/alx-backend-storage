#!/usr/bin/env python3
""" Stores the cache class """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache Class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self: 'Cache', data: Union[str, bytes, int, float]) -> str:
        """ Generates and returns a random key """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self, key: str, 
            fn: callable = None
            ):
        """ retrives values from redis """
        data = self._redis.get(key)
        if data is not None:
            return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """ get data and converts to string """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ get data and converts to integer """
        return self.get(key, fn = lambda x: int(x))
