from dimacs import loadDirectedWeightedGraph

class Node:
  def __init__(self, idx):
    self.idx = idx
    self.out = set()                    # set of neighbours

  def connect_to(self, v):              # add edge between node (u) and node (v)
    self.out.add(v)

def lex_bfs(G, start = 1):
    V = len(G)

    full_set = set([G[i] for i in range(1, V) if i != start])
    start_set = set({G[start]})

    sets = [full_set, start_set]
    result = []

    while len(sets) > 0: 
        u = sets[-1].pop()
        result.append(u.idx)

        new_sets = []
        for X in sets:
            Y = set()
            K = set()
            
            for v in X:
                if v in u.out:
                    Y.add(v)
                else:
                    K.add(v)

            new_sets.append(K)
            new_sets.append(Y)    
        
        while len(new_sets) > 0 and not new_sets[-1]:
            new_sets.pop()

        sets = new_sets

    return result

def run(name):
    (V, L) = loadDirectedWeightedGraph(name)

    G = [None] + [Node(i) for i in range(1, V + 1)]  # żeby móc indeksować numerem wierzchołka

    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)

    return G, lex_bfs(G)