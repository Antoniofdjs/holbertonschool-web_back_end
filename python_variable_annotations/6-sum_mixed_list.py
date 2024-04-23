#!/usr/bin/env python3
"""
    Write a type-annotated function sum_mixed_list which takes a list
    'input_list' of floats as argument and returns their sum as a float.
"""

from typing import Union


def sum_mixed_list(mxd_list: list[Union[int, float]]) -> float:
    """
        Makes the sum of the 'mxd_list' and returns it as float
    """

    return float(sum(mxd_list))
