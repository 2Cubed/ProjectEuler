"""Solution to Project Euler Problem 4
https://projecteuler.net/problem=4
"""

DIGITS = 3


def compute(digits=DIGITS):
    """Find the largest palindromic number made from the product of two numbers
    of lengths `digits`.
    """

    values = list()

    for num1 in range(10**digits, 10**(digits-1), -1):
        for num2 in range(10**digits, 10**(digits-1), -1):
            product = num1 * num2
            if str(product) == str(product)[::-1]:
                values.append(product)

    return max(values)
