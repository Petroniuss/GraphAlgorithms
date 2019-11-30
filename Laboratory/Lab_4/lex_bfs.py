from dimacs import *


class Node:
  def __init__(self, idx):
    self.idx = idx
    self.out = set()              # zbiór sąsiadów

  def connect_to(self, v):
    self.out.add(v)

def lex_bfs(G, start):
    V = len(G) 

    visited = [False] * V

    full_set = set([i for i in range(1, V+1) if i != start])
    start_set = set({start})

    sets = [full_set, start_set]
    result = []

    while len(sets) > 0:
        u = sets[-1].pop()
        result.append(u)
        visited[u] = True

        new_sets_list = []

        for set in sets[:]:
            neigh_set = set()
            not_neigh_set = set()

            for node in set:
                if not visited[node.idx]:
                    if node in u.out():
                        neigh_set.add(node)
                    else:
                        not_neigh_set.add(node)

            new_sets_list.append(not_neigh_set)
            new_sets_list.append(neigh_set)

        sets = new_sets_list

    return result

def run(name):
    (V, L) = loadDirectedWeightedGraph(name)

    G = [None] + [Node(i) for i in range(1, V + 1)]  # żeby móc indeksować numerem wierzchołka

    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)
