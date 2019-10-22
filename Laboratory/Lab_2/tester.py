from ford_fulkerson import ford_fulkerson
from dimacs import load_solution
import os

ex_1_tests_directory = "Laboratory\\Lab_2\\tests\\flow"
ex_1_tests = [os.fsdecode(file) for file in os.listdir(ex_1_tests_directory)]

for test in ex_1_tests:
    print("Testing...", test)

    test_path = ex_1_tests_directory + "\\" + test

    solution = load_solution(test_path)
    actual = ford_fulkerson(test_path)

    print("solution {0}, actual {1}".format(solution, actual), end=" ")
    if actual == solution:
        print(u"\u2713")