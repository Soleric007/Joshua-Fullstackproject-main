from typing import List

def paginate(items: List, page: int = 1, page_size: int = 10):
    """Simple pagination helper"""
    start = (page - 1) * page_size
    end = start + page_size
    total = len(items)
    return {
        "page": page,
        "page_size": page_size,
        "total": total,
        "items": items[start:end]
    }