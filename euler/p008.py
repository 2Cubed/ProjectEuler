"""Solution to Project Euler Problem 8
https://projecteuler.net/problem=8
"""

from functools import reduce
from operator import mul

FILENAME = "resources/p008_number.txt"

SEGMENT_SIZE = 13


def compute(filename=FILENAME, segment_size=SEGMENT_SIZE):
    """Compute the largest product of `segment_size` adjacent digits in the
    number given in the file `filename`.
    """

    number = open(filename, 'r').read().strip()

    segments = set(
        number[index:index+segment_size] for index in range(len(number)-1)
    )

    products = tuple(
        reduce(mul, tuple(int(digit) for digit in segment))
        for segment in segments
    )

    return max(products)
