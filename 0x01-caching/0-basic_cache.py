#!/usr/bin/env python3
"""Import module/lib"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache inherits from BaseCaching"""
    def __init__(self):
        """Instanciate the class"""
        BaseCaching.__init__(self, cache_data)
        self.cache_data = {}

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data"""
        if key or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
