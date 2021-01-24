"""
Дан неориентированный связный взвешенный граф. Найдите кратчайшее расстояние от первой вершины до всех вершин.
______________
input:
4 5
1 2 1
1 3 5
2 4 8
3 4 1
2 3 3

output:
0 1 4 5
"""

from collections import defaultdict
from math import inf
import heapq


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.distance = defaultdict(int)

    def add(self, u, v):
        self.graph[u].append(v)

    def dijkstra(self):
        self.distance[1] = 0
        ml = list()
        heapq.heappush(ml, (0, 1))
        while ml:
            dist, u = heapq.heappop(ml)

            if dist != self.distance[u]:
                continue
            if self.distance[u] == inf:
                break

            for vert, weight in self.graph[u]:
                if self.distance[u] + weight < self.distance[vert]:
                    self.distance[vert] = self.distance[u] + weight
                    heapq.heappush(ml, (self.distance[vert], vert))


def read_graph():
    n, m = map(int, input().split())

    g = Graph()

    for _ in range(m):
        b, e, weight = map(int, input().split())
        g.add(b, (e, weight))
        g.add(e, (b, weight))

    for i in range(1, n + 1):
        g.distance[i] = inf

    return g


if __name__ == '__main__':
    G = read_graph()
    G.dijkstra()
    for value in G.distance.values():
        print(value, end=' ')