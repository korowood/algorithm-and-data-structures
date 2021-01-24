"""
Вам дан взвешенный ориентированный граф и вершина s в нём.
Для каждой вершины графа u выведите длину кратчайшего пути от вершины s до вершины u.
______________
input:
6 7 1
1 2 10
2 3 5
1 3 100
3 5 7
5 4 10
4 3 -18
6 1 -1

output:
0
10
-
-
-
*
"""

from collections import defaultdict
from math import inf


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.distance = defaultdict(int)
        self.p = defaultdict(int)
        self.edges = []
        self.visited = defaultdict(bool)
        self.access = defaultdict(bool)

    def add(self, u_, v_):
        self.graph[u_].append(v_)

    def dfs(self, v_):
        self.access[v_] = False
        self.visited[v_] = True
        for u_, w_ in self.graph[v_]:
            if not self.visited[u_]:
                self.dfs(u_)


def read_graph(n, m):
    # n, m, s = map(int, input().split())

    g = Graph()

    for _ in range(m):
        b, e, weight = map(int, input().split())
        g.add(b, (e, weight))
        g.edges.append((b, e, weight))

    for i in range(1, n + 1):
        g.distance[i] = inf
        g.p[i] = -1
        g.visited[i] = False
        g.access[i] = True

    g.distance[s] = 0
    return g


def update_dist(graph, n_):
    for k in range(1, n_ + 1):
        for u_, v_, w_ in graph.edges:
            if graph.distance[u_] + w_ < graph.distance[v_]:
                graph.distance[v_] = graph.distance[u_] + w_
                graph.p[v_] = u_


def ans(graph):
    for key, value in graph.distance.items():
        if value == inf:
            print("*")
        elif not G.access[key]:
            print("-")
        else:
            print(value)


if __name__ == '__main__':
    n, m, s = map(int, input().split())
    G = read_graph(n, m)
    update_dist(G, n)

    for u, v, w in G.edges:
        if G.distance[v] > G.distance[u] + w:
            G.dfs(v)

    ans(G)
    # for key, value in G.distance.items():
    #     if value == inf:
    #         print("*")
    #     elif not G.access[key]:
    #         print("-")
    #     else:
    #         print(value)
