import random 

class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight
        self.next = None

    def __str__(self):
        return "Edge[to: {}, weight: {}]".format(str(self.to), str(self.weight))

#
#   Directed graph with weighted edges, consisting of V vertices.
# 
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest, weight):
        edge = Edge(dest, weight)
        edge.next = self.graph[src]
        self.graph[src] = edge

    def show_graph(self):
        for i in range(self.V):
            print("Vertex {}".format(i), end="")
            
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp))
                temp = temp.next
            print("")

    def containsEdge(self, fromVertex, toVertex):
        flag, tmp = False, self.graph[fromVertex]

        while (not flag) and tmp:
            if tmp.to == toVertex:
                flag
            tmp = tmp.next

        return flag

    def depth_first_search(self):
        visited = [False] * self.V

        for src in range(0, V):
            if not visited[src]:
                self.__dfs_recursive(visited, src)


    def __dfs_recursive(self, visited, src):
        visited[src] = True
        neigh = self.graph[src]

        print("Visted vertex {} \n".format(src))

        while neigh:
            if not visited[neigh.to]:
                self.__dfs_recursive(visited, neigh.to)
            neigh = neigh.next

    @staticmethod
    def random_graph(V):
        graph = Graph(V)
        edges_number, i = random.randint(0, V * V), 0

        while i < edges_number:
            fromV = random.randint(0, V - 1)
            toV = random.randint(0, V - 1)
            weight = random.randint(1, V * V)

            if (not graph.containsEdge(fromV, toV)):
                graph.add_edge(fromV, toV, weight)
                i = i + 1

        return graph



if __name__ == "__main__":
    V = 5
    graph = Graph.random_graph(V)
  
    graph.show_graph() 
    graph.depth_first_search()