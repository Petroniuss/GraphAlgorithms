import collections

#   First Lecture: Maximum Flow Problem

#   Ford-Fulkerson/Edmonds-Karp algorithm.
#   
#   Input: adjacency matrix.
#   Output: maximum flow.
class ResidualGraph:

    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
        self.residual_graph = [[[row[i], 0] for i in range(0, self.V)] for row in self.graph] # we set c as in input and f to 0

    def breadth_first_search(self, s, t, parent):
        visited = [False] * self.V
        queue = collections.deque()

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.popleft()

            for i, v in enumerate(self.residual_graph[u]):
                cf = v[0] - v[1]
                if (not visited[i]) and (cf > 0):
                    visited[i] = True
                    parent[i] = u
                    queue.append(i)

        return visited[t]

    def edmonds_karp(self, source, sink):
        s = source
        t = sink

        parent = [-1] * self.V
        max_flow = 0

        while self.breadth_first_search(s, t, parent):
            u = t
            v = parent[u]
            bottleneck = float("Inf")  

            while u != s:
                tmp = self.residual_graph[v][u]
                cf = tmp[0] - tmp[1]
                bottleneck = min(bottleneck, cf)
                u = v
                v = parent[v]

            max_flow += bottleneck

            u = t
            v = parent[u]

            while u != s:
                self.residual_graph[v][u][1] += bottleneck
                self.residual_graph[u][v][1] -= bottleneck
                u = v
                v = parent[v]
        
        return max_flow


if __name__ == "__main__":

    graph = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]] 
    g = ResidualGraph(graph)
    source, sink = 0, 5

    print(g.edmonds_karp(source, sink))
#
# [
# [[c, f]]
#   ]
#
#
#
#
#
