from dimacs import *

class Subset:
    def __init__(self, parent):
        self.parent = parent
        self.rank = 0


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



### Main ###
(V, L) = loadWeightedGraph(r"Graphs\Laboratory\Lab_1\Tests\g1")

for (u, v, w) in L:
    print("Edge[From: ", u, ", to: ", v, ", weight: ", w, "]", sep="")