from ford_fulkerson import ford_fulkerson
from dimacs import loadDirectedWeightedGraph

def edge_connectivity(test):
    (V, _) = loadDirectedWeightedGraph(test)
    minimum = float("inf")

    for s in range(1, V + 1):
        t = s + 1
        
        while t <= V:
            v = ford_fulkerson(test, s, t)
            
            if v < minimum:
                minimum = v

            t = t + 1
    
    return minimum