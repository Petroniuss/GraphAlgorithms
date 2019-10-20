from queue import PriorityQueue
from collections import deque


class Graph:
    def __init__(self, V, E):
        self.V = V
        self.G = [deque() for _ in range(self.V + 1)]

        for (x, y, w) in E:
            self.G[x].appendleft((y, w))

Q = PriorityQueue()
