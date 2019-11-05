from ford_fulkerson import ford_fulkerson
from dimacs import loadWeightedGraph

"""
    Naive solution with O(V^3 E^2) time complexity. 
"""
def edge_connectivity(test):
    (V, _) = loadWeightedGraph(test)
    minimum = float("inf")

    for s in range(1, V):
        t = s + 1
        
        while t <= V:
            v = ford_fulkerson(test, s, t)
            
            if v < minimum:
                minimum = v

            t = t + 1
    
    return minimum