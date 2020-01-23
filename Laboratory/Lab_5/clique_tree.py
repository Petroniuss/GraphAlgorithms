from lex_bfs import run

class Node:    
    def __init__(self, idx):
        self.idx = idx
        self.children = []
        self.parent = None

    def add_kid(self, kid: Node):
        self.children.append(kid)

    def set_parent(self, parent: Node):
        self.parent = parent

def build_tree(G, order, rn):
    V = len(G)
    nodes = [Node(i) for i in range(1, V)]
    root = None

    for i in range(1, V):
        if len(rn[i]) == 0:
            root = nodes[i]
        else: 
            rightmost = rn[i][-1]
            nodes[i].set_parent(nodes[rightmost])
            nodes[rightmost].add_kid(nodes[i])
    
    return root 

def calc_rn(G, order):
    V = len(G)
    rn = [[] for i in range(1, V)]

    for u in range(1, V):
        neighs = G[u].out
        i = index_of_u(order, u)

        for e in order[:i]:
            if e in neighs:
                rn[u].append(e)

    return rn

def index_of_u(order, u):
    for i, e in enumerate(order):
        if e == u:
            return i


def check_if_u_exists_before_i(u, i, order):
    for v in order[:i]:
        if v == u:
            return True
    return False

def run_clique_tree(test):
    G, order = run(test)
    rn = calc_rn(G, order)
    root = build_tree(G, order, rn)

