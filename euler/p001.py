"""Solution to Project Euler Problem 1
https://projecteuler.net/problem=1
"""

NUMBERS = 3, 5
MAXIMUM = 1000


def compute(*numbers, maximum=MAXIMUM):
    """Compute the sum of the multiples of `numbers` below `maximum`."""

    if not numbers:
        numbers = NUMBERS

    multiples = tuple(set(range(0, maximum, number)) for number in numbers)

    return sum(set().union(*multiples))
