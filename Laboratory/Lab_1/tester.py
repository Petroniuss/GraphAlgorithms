from bin_search_solve import solve as bin_search_solve
from find_union_solve import solve as find_union_solve
from dimacs import load_solution
import os

directory = os.fsencode("Laboratory\\Lab_1\\Tests\\")
tests = [os.fsdecode(file) for file in os.listdir(directory)]

(success_mark, failure_mark) = (u"\u2713", u"\u274C")
(bin_search_success, find_union_success) = (0, 0) 

for test in tests:
    solution = load_solution(test)

    print("Testing:", test, "...")

    if bin_search_solve(test) == solution:
      bin_search_success = bin_search_success + 1
    if find_union_solve(test) == solution:
      find_union_success = find_union_success + 1
    
    print("Tested: ", test, success_mark)

print("Binary Search Solution passed", bin_search_success, "/", len(tests), "-" * 28)
print("Union Find Solution passed", find_union_success, "/", len(tests), "-" * 30)