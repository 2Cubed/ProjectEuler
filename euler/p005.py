from fractions import gcd
from functools import reduce

MAXIMUM = 20


def compute(maximum=MAXIMUM):
    """Compute the LCM of all integers from 1 to `maximum`."""

    return int(reduce(lambda x, y: (x*y)/gcd(x, y), range(1, maximum + 1)))
