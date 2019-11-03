from ford_fulkerson import ford_fulkerson
from dimacs import load_solution
import os

"""
    To run  test in top directory run: py Laboratory/Lab_2/tester.py
"""

ex_1_tests_directory = "Laboratory\\Lab_2\\tests\\flow"
ex_1_tests = [os.fsdecode(file) for file in os.listdir(ex_1_tests_directory)]
ex_1_success = 0

print("-" * 10 + "TESTS" + "-" * 10)

for test in ex_1_tests:
    print("Testing...", test)

    test_path = ex_1_tests_directory + "\\" + test

    solution = load_solution(test_path)
    actual = ford_fulkerson(test_path)

    print("solution {0}, actual {1}".format(solution, actual), end = " ")

    if actual == solution:
        print(u"\u2713")
        ex_1_success = ex_1_success + 1

print("-" * 50)
print("Finished testing Ford_Fulkerson {0}/{1} ".format(ex_1_success, len(ex_1_tests)) + u"\u2713")
print("-" * 50)