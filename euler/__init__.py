"""Solve the Project Euler problems using functional Python.
https://projecteuler.net/archives
"""

from importlib import import_module

from os import listdir
from os.path import abspath, dirname
from re import match


SOLVED = set(
    int(m.group(1))
    for f in listdir(abspath(dirname(__file__)))
    for m in (match(r"^p(\d{3})\.py$", f),) if m
)


def compute(problem: int):
    """Compute the answer to problem `problem`."""

    assert problem in SOLVED, "Problem currently unsolved."

    module = import_module("euler.p{:03d}".format(problem))
    return module.compute()
