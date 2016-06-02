"""Solution to Project Euler Problem 3
https://projecteuler.net/problem=3
"""

from math import floor, sqrt

NUMBER = 600851475143


def compute(number=NUMBER):
    """Find the largest prime factor of `number`."""

    factors = list()

    for test_prime in range(3, floor(sqrt(number)), 2):
        if number % test_prime == 0:
            factors.append(test_prime)
            number /= test_prime
            if number == 1:
                break

    return factors[-1]
