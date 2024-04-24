#!/usr/bin/env python3
"""
    Write a type-annotated function make_multiplier that takes a
    float multiplier as argument and returns a function that
    multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Function that returns another function
        Returns a function that takes a float and returns a float
    """

    def multiply(n: float) -> float:  # type-annotated function
        """"
            Returns the product of a float and multiplier

            n: float

            return: product of n and multiplier
        """
        return n * multiplier
    return multiply
