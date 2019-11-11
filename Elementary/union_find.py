from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.neighs = defaultdict(list)

    def add_edge(self, u, v):
        self.neighs[u].append(v)


class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

def is_cycle(graph):
    subsets = [Subset(u, 0) for u in range(graph.V)]

    for u in range(graph.V):
        u_repr = find(subsets, u)

        for v in graph.neighs[u]:
            v_repr = find(subsets, v)

            if u_repr == v_repr:
                return True
            else:
                union(subsets, u, v)

    return False


def find(subsets, v):
    if subsets[v].parent != v:
        subsets[v].parent = find(subsets, subsets[v].parent)
    
    return subsets[v].parent

def union(subsets, u, v):
    u_rank, v_rank = subsets[u].rank, subsets[v].rank
    u_parent, v_parent = find(subsets, u), find(subsets, v)

    if u_rank < v_rank:
        subsets[u_parent].parent = v_parent
    elif u_rank > v_rank:
        subsets[v_parent].parent = u_parent
    else:
        subsets[u_parent].parent = v_parent
        subsets[v_parent].rank = subsets[v_parent] + 1