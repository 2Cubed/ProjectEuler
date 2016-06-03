"""Solution to Project Euler Problem 6
https://projecteuler.net/problem=6
"""

MAXIMUM = 100


def compute(maximum=MAXIMUM):
    """Compute the difference between the square of the sum and the sum of the
    squares of the first `maximum` natural numbers.
    """

    return sum(range(1, maximum+1))**2 - sum(n**2 for n in range(1, maximum+1))
