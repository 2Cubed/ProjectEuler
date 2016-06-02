"""Solution to Project Euler Problem 5
https://projecteuler.net/problem=5

gcd, lcm, and lcmm functions by J.F. Sebastian.
http://stackoverflow.com/a/147539/6119465
"""

from functools import reduce

MAXIMUM = 20


def gcd(num1, num2):
    """Return greatest common divisor using Euclid's Algorithm."""
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def lcm(num1, num2):
    """Return lowest common multiple."""
    return num1 * num2 // gcd(num1, num2)


def lcmm(*args):
    """Return LCM of args."""
    return reduce(lcm, args)


def compute(maximum=MAXIMUM):
    """Compute the LCM of all integers from 1 to `maximum`."""

    return lcmm(*range(1, maximum + 1))
