"""Test the solutions to the Project Euler problems."""

from json import load
from time import time

from euler import SOLVED, compute

ANSWERS = load(open("resources/answers.json", 'r'))


for problem in SOLVED:
    start_time = time()
    computed = compute(problem)
    end_time = time()

    assert end_time - start_time <= 60, "solution took too long to execute"

    assert computed == ANSWERS[str(problem)], """incorrect solution
  Problem {problem}:
    Computed: {computed}
    Correct: {correct}""".format(
        problem=problem,
        computed=computed,
        correct=ANSWERS[str(problem)])
