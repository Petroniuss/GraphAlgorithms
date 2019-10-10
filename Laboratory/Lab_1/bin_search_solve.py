from collections import deque
from dimacs import *

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.G = [deque()] * (V + 1)
        
        for (u, v, w) in E:
            self.add_edge(u, v, w)
        
    
    def add_edge(self, u, v, w):
        self.G[u].appendleft((v, w))


def depth_first_search(graph, s, t, minWeight):
    visited = [False] * (graph.V + 1)
    depth_first_search_visit(graph, visited, minWeight, s)

    return visited[t] 

def depth_first_search_visit(graph, visited, minWeight, u):
    visited[u] = True

    for (v, w) in graph.G[u]:
        if not visited[v] and w >= u:
            depth_first_search(graph, visited, minWeight, v)


def bin_search_solution(E, V, s, t):
    L, R = 0, V
    graph = Graph(E, V)
    flow = -1

    while L <= R:
        m = (L + R) / 2

        if depth_first_search(graph, s, t, E[m][2]):
            L = m + 1
            flow = E[m][2]
        else:
            R = m - 1

    return flow


#--------------------Solution--------------------------#
(V, E) = loadWeightedGraph(r"Laboratory\Lab_1\Tests\g1")
E.sort(key=lambda edge: edge[2])

solution = bin_search_solution(E, V, 1, 2)

print(solution)