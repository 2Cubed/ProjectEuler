"""Solution to Project Euler Problem 9
https://projecteuler.net/problem=9
"""

ABC_SUM = 1000


def compute(abc_sum=ABC_SUM):
    """Compute the product *abc* of the first Pythagorean triplet a²+b²=c² for
    which the sum of a, b, and c is equal to `abc_sum`.
    """

    for c_value in range(abc_sum):
        for a_value in range(abc_sum - c_value):
            if a_value**2 + (abc_sum - c_value - a_value)**2 == c_value**2:
                return a_value * (abc_sum - c_value - a_value) * c_value
