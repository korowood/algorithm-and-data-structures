"""
Ваша задача — найти наибольшее количество воды, которое за единицу времени может протекать между источником и стоком,
а также скорость течения воды по каждой из труб.
______________
input:
2
2
1 2 1
2 1 3

output:
4
1
-3
"""

import collections


class Edge:
    def __init__(self, u, v, capacity, flow=0):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = flow


class Graph:

    def __init__(self, ):
        self.graph = list()
        self.numNodes = int()
        self.nodeName = dict()
        self.nodeIndex = dict()
        self.edges = list()
        self.source = int()
        self.sink = int()

    def BFS(self, camino):

        visited = [False] * self.numNodes
        queue = collections.deque()

        queue.append(self.source)
        visited[self.source] = True

        while queue:

            u = queue.popleft()

            for ind, val in enumerate(self.graph[u]):

                if val > 0 and not visited[ind]:
                    visited[ind] = True
                    camino[ind] = u
                    queue.append(ind)

        return visited[self.sink]

    def EdmondsKarp(self):

        camino = [-1] * (self.numNodes)

        flujoMaximo = 0

        while self.BFS(camino):

            flujoCamino = float("Inf")

            s = self.sink
            while s != self.source:
                flujoCamino = min(flujoCamino, self.graph[camino[s]][s])
                s = camino[s]

            v = self.sink
            while v != self.source:
                u = camino[v]
                self.graph[u][v] -= flujoCamino
                self.graph[v][u] += flujoCamino
                v = camino[v]

            flujoMaximo += flujoCamino

        return flujoMaximo


