from dimacs import *

class Subset:
    def __init__(self, parent):
        self.parent = parent
        self.rank = 0





### Main ###
(V, L) = loadWeightedGraph(r"Graphs\Laboratory\Lab_1\Tests\g1")

for (u, v, w) in L:
    print("Edge[From: ", u, ", to: ", v, ", weight: ", w, "]", sep="")