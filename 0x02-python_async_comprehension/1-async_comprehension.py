#!/usr/bin/env python3
"""Async Comprehensions"""

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Iterate through a generator"""

    result = [x async for x in async_generator()]

    return result
