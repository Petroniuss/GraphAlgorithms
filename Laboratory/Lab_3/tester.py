from dimacs import load_solution
from edge_connectivity import edge_connectivity
import os

"""
    To exectute in top directory run: py Laboratory/Lab_3/tester.py
"""

ex_1_tests_directory = "Laboratory\\Lab_3\\tests\\connectivity"
ex_1_tests = [os.fsdecode(file) for file in os.listdir(ex_1_tests_directory)]
ex_1_success = 0

print("-" * 20 + "TESTS" + "-" * 20)

for test in ex_1_tests:
    print("Testing...", test)

    test_path = ex_1_tests_directory + "\\" + test

    actual = edge_connectivity(test_path)
    solution = load_solution(test_path)

    print("solution {0}, actual {1}".format(solution, actual), end = " ")

    if actual == solution:
        print(u"\u2713", end= "")
        ex_1_success = ex_1_success + 1
    
    print("\n")

print("-" * 50)
print("Finished testing edge connectivity algorithm {0}/{1} ".format(ex_1_success, len(ex_1_tests)) + u"\u2713")
print("-" * 50)