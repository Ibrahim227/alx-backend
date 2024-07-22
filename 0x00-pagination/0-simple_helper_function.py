#!/usr/bin/env python3
"""Import required module/lib"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[()]:
    """Return a tuple of size two containing a start index and end index"""
    return (page, page_size)
