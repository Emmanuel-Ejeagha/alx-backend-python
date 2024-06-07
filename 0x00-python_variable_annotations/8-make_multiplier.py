#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multipler: float) -> Callable[[float], float]:
    """Return a function that multiplies a float"""
    def num_func(number: float) -> float:
        """The function that multiplies a float with a multiple"""
        return number * multipler
    return num_func
