#!/usr/bin/env python3
"""function sum_mixed_list decleration"""


from typing import Tuple, Union


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """return a sum of all nums inside a list"""
    def multiplies(n: float):
        """
        multiply two number
        """
        return n * multiplier
    return multiplies
