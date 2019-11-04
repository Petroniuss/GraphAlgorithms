from collections import deque
from dimacs import loadDirectedWeightedGraph

"""
    Edmonds-Karp implementation of Ford-Fulkerson algorithm.
"""
class Graph:

    ### Edge is represented by tuple: (to, flow, capacity) ###
    def __init__(self, E, V):
        self.V = V
        self.G = [[] for _ in range(V + 1)] 
        
        for (u, v, capacity) in E:
            self.G[u].append((v, 0, capacity))

            if not self.contains_edge(v, u):
                self.G[v].append((u, 0, 0))


    def contains_edge(self, u, v):
        for (to, _, _) in self.G[u]:
            if to == u:
                return True
        
        return False

    def find_edge_index(self, u, v):
        for i, (to, _, _) in enumerate(self.G[u]):
            if to == v:
                return i

    def update_edge(self, u, v, flow):
        index, f, cpc = -1, flow, -1

        for i, (to, _, c) in enumerate(self.G[u]):
            if to == v:
                index, cpc = i, c 
                break
        
        self.G[u][index] = (v, f, cpc)


    def find_edge(self, u, v):
        for edge in self.G[u]:
            if edge[0] == v:
                return edge

def find_path(graph, parent, s , t):
    visited = [False] * (graph.V + 1)
    visited[s] = True
    
    Q = deque()
    Q.append(s)

    while Q:
        u = Q.popleft()
        for (v, flow, capacity) in graph.G[u]:
            cf = capacity - flow
            if (not visited[v]) and cf > 0:
                parent[v] = u
                visited[v] = True
                Q.append(v)   

    return visited[t]


def ford_fulkerson(test):
    (V, L) = loadDirectedWeightedGraph(test)
    
    graph = Graph(L, V)
    parent = [-1 for _ in range (V + 1)]
    s, t = 1, V

    while find_path(graph, parent, 1, V):
        v = t
        min_cf = float("inf")

        while v != s:
            u = parent[v]
            (_, flow, capacity) = graph.find_edge(u, v)

            cf = capacity - flow

            if cf < min_cf:
                min_cf = cf
            v = u

        v = t
        
        while v != s:
            u = parent[v]

            u_v_edge = graph.find_edge(u, v)
            v_u_edge = graph.find_edge(v, u)

            u_v_flow = u_v_edge[1] + min_cf
            v_u_flow = v_u_edge[1] - min_cf

            graph.update_edge(u, v, u_v_flow)
            graph.update_edge(v, u, v_u_flow)

            v = u

    maxium_flow = 0

    for (_, f, _) in graph.G[s]:
        maxium_flow = maxium_flow + f

    return maxium_flow
