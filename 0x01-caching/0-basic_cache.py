#!/usr/bin/env python3
"""Import module/lib"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache inherits from BaseCaching"""
    def __init__(self):
        """Instanciate the class"""
        BaseCaching.__init__(self, cached_data)
        self.cached_data = {}

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data"""
        if key or item is None:
            pass
        else:
            self.cached_data[key] = item

    def get(self, key);
        """Must return the value in self.cache_data linked to key"""
        if key is None or key not in self.cached_data:
            return None
        else:
            return self.cached_data[key]
