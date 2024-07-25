#!/usr/bin/env python3
"""Import Module/Lib"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class LIFOCache, inherits from BaseCaching"""
    def __init__(self):
        """initalize the class"""
        super().__init__()
        self.access = []

    def put(self, key, item):
        """Put method"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            popItem = self.access.pop()
            del self.cache_data[popItem]
            print("DISCARD: {}".format(popItem))

        self.access.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get method"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
