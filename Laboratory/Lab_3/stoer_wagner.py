from dimacs import loadWeightedGraph

class Node:
  def __init__(self):
    self.edges = {}    # słownik par mapujący wierzchołki do których są krawędzie na ich wagi

  def addEdge( self, to, weight):
    self.edges[to] = self.edges.get(to,0) + weight  # dodaj krawędź do zadanego wierzchołka
                                                    # o zadanej wadze; a jeśli taka krawędź
                                                    # istnieje, to dodaj do niej wagę

  def delEdge( self, to ):
    del self.edges[to]                              # usuń krawędź do zadanego wierzchołka


class Graph:

    def __init__(self, V, L):
        self.G = [ Node() for i in range(V + 1) ]
        self.V = V

        for (x,y,c) in L:
            self.G[x].addEdge(y,c)
            self.G[y].addEdge(x,c)

    def add_edge(self, u, v, weight):
        self.G[u].addEdge(v, weight)
    
    def delete_edge(self, u, v):
        self.G[u].delEdge(v)

    def print_graph(self):
        for (u, node) in enumerate(self.G):
            for v in range(1, self.V + 1):
                weight = node.edges.get(v, 0)
                
                if weight != 0:
                    print(f"From: {u}, to: {v}, weight: {weight}")


# def stoer_wagner(test):
test_dir = "Laboratory\\Lab_3\\tests\\connectivity"

(V,L) = loadWeightedGraph(test_dir + "\\simple")        # wczytaj graf
graph = Graph(V, L)

graph.print_graph()

