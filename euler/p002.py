"""Solution to Project Euler Problem 2
https://projecteuler.net/problem=2
"""

MAXIMUM = 4e6


def compute(maximum=MAXIMUM):
    """Compute the sum of the even-valued terms of the Fibonacci sequence
    less than or equal to `maximum`.
    """

    fibonacci = [0, 1]

    while fibonacci[-1] <= maximum:
        fibonacci.append(sum(fibonacci[-2:]))

    return sum(fibonacci[::3])
