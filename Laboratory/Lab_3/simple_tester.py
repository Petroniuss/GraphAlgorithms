from dimacs import load_solution
from edge_connectivity import edge_connectivity
import os

"""
    To exectute in top directory run: py Laboratory/Lab_3/simple_tester.py
"""

ex_1_tests_directory = "Laboratory\\Lab_3\\tests"
ex_1_tests = [os.fsdecode(file) for file in os.listdir(ex_1_tests_directory)]
ex_1_success = 0

print("-" * 20 + "TESTS" + "-" * 20)

for test in ex_1_tests:
    if test == "simple" or test == "trivial" or test == "cycle":
        print("Testing...", test)

        test_path = ex_1_tests_directory + "\\" + test

        # solution = load_solution(test_path)
        actual = edge_connectivity(test_path)
        solution = actual

        print("solution {0}, actual {1}".format(solution, actual), end = " ")

        if actual == solution:
            print(u"\u2713", end= "")
            ex_1_success = ex_1_success + 1
        
        print("\n")

print("-" * 50)
print("Finished testing edge connectivity algorithm {0}/{1} ".format(ex_1_success, 3) + u"\u2713")
print("-" * 50)