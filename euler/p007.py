"""Solution to Project Euler Problem 7
https://projecteuler.net/problem=7
"""

INDEX = 10001


def compute(index=INDEX):
    """Find the `index`th prime number."""

    primes = [2]
    test_number = 3

    while len(primes) < index:
        for prime in primes:
            if test_number % prime == 0:
                break
        else:
            primes.append(test_number)
        test_number += 2

    return primes[-1]
