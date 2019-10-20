from dimacs import *

class Subset:
    def __init__(self, parent):
        self.parent = parent
        self.rank = 0

class Graph:
    # Edge: (from, to, weight)
    def __init__(self, V, edges):
        self.V = V
        self.edges = edges 

    def print_edges(self):
        for (u, v, w) in self.edges:
            print("Edge[From: ", u, ", to: ", v, ", weight: ", w, "]", sep="")  

    def sort_edges(self):
        self.edges.sort(key = lambda edge: edge[2], reverse=True)


def find(subsets, u):
    if u != subsets[u].parent:
        subsets[u].parent = find(subsets, subsets[u].parent)    
    
    return subsets[u].parent

def union(subsets, u, v):
    u_repr, v_repr = find(subsets, u), find(subsets, v)
    u_rank, v_rank = subsets[u_repr].rank, subsets[v_repr].rank

    if u_rank < v_rank:
        subsets[u_repr].parent = v_repr
    elif v_rank < u_rank:
        subsets[v_repr].parent = u_repr
    else:
        subsets[u_repr].parent = v_repr
        subsets[v_repr].rank = subsets[v_repr].rank + 1

### Main ###
# We assume that s = 1, t = 2.
def solve(test):
    (V, E) = loadWeightedGraph(r"Laboratory\Lab_1\Tests" + "\\" + test)
    subsets = [Subset(u) for u in range(V + 1)]
    s, t = 1, 2

    graph = Graph(V, E)
    graph.sort_edges()

    for (u, v, w) in graph.edges:
        union(subsets, u, v)

        s_repr = find(subsets, s)
        t_repr = find(subsets, t)

        if s_repr == t_repr:
            return w

    return -1

