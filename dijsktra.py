class Graph:
    
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)

    def dijsktra(self, s):
        distances = [float("inf")] * self.V
        included = [False] * self.V

        distances[s] = 0

        for _ in range(self.V - 1):
            u = min(distances, included)
            included[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and (not included[v]) and \
                 (distances[u] + self.graph[u][v] < distances[v]):
                    distances[v] = distances[u] + self.graph[u][v]

        return distances

    def min(self, distances, included):
        min = float("inf")
        min_index = -1

        for u in range(self.V):
             if included[u] and distances[u] < min:
                 min_index = u
                 min = distances[u]

        return min_index

