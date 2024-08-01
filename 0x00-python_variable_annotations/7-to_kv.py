#!/usr/bin/env python3
"""function sum_mixed_list decleration"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a sum of all nums inside a list"""
    return (k, v**2)
