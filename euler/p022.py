"""Solution to Project Euler Problem 22
https://projecteuler.net/problem=22
"""

from string import ascii_uppercase
LETTER_MAP = dict((v, k) for k, v in enumerate(ascii_uppercase, 1))

FILENAME = "resources/p022_names.txt"


def compute(filename=FILENAME):
    """Compute the total of all "name scores" (see problem) in `filename`."""

    names = sorted(open(filename, 'r').read()[1:-1].split(r'","'))

    return sum(
        position*sum(LETTER_MAP[letter] for letter in name)
        for position, name in enumerate(names, 1)
    )
