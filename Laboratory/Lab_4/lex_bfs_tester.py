from lex_bfs import run
from dimacs import checkLexBFS
import os

"""
    To exectute in top directory run: py Laboratory/Lab_4/lex_bfs_tester.py
"""

ex_1_tests_directory = "Laboratory\\Lab_4\\tests\\maxclique"
ex_1_tests = [os.fsdecode(file) for file in os.listdir(ex_1_tests_directory)]
ex_1_success = 0

print("-" * 20 + "TESTS" + "-" * 20)

for test in ex_1_tests:
    print("Testing...", test)

    test_path = ex_1_tests_directory + "\\" + test

    G, vs = run(test_path)

    print(vs, end="")

    if checkLexBFS(G, vs):
        print('', u"\u2713", end= "")
        ex_1_success = ex_1_success + 1
    
    print("\n")

print("-" * 50)
print("Finished testing lex-bfs {0}/{1} ".format(ex_1_success, len(ex_1_tests)) + u"\u2713")
print("-" * 50)

