#!/usr/bin/env python3
"""Import Module/Lib"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class LIFOCache, inherits from BaseCaching"""
    def __init__(self):
        """initalize the class"""
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """Put method"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            popItem = self.cache_keys.pop()
            del self.cache_data[popItem]
            print("DISCARD: {}".format(popItem))

        self.cache_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get method"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
