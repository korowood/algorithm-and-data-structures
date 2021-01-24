"""
Требуется найти количество ребер в конденсации ориентированного графа.
______________
TEST1
input:
4 4
2 1
3 2
2 3
4 3

output:
2
"""

from sys import setrecursionlimit
import threading


class Graph:
    def __init__(self, n: int):
        self.size = n
        self.graph = [set() for _ in range(n)]
        self.used = [False] * n
        self.tout = [0] * n
        self.t = 0
        self.t_sort = []
        self.components = [0] * n
        self.components_size = 0

    def add_adjacent_vertex(self, vertex: int, adjacent: int):
        self.graph[vertex].add(adjacent)

    def dfs_topological(self, vertex: int):
        self.used[vertex] = True
        for adj_vertex in self.graph[vertex]:
            if not self.used[adj_vertex]:
                self.dfs_topological(adj_vertex)
        self.t_sort.append(vertex)

    def topological_sort(self):
        for vertex in range(self.size):
            if not self.used[vertex]:
                self.dfs_topological(vertex)
        self.t_sort = list(reversed(self.t_sort))

    def reverse(self):
        g_rev = Graph(self.size)
        for vertex in range(self.size):
            for adj_vertex in self.graph[vertex]:
                g_rev.add_adjacent_vertex(adj_vertex, vertex)
        return g_rev

    def dfs_components(self, vertex: int, current_component: int):
        self.components[vertex] = current_component
        for adj_vertex in self.graph[vertex]:
            if self.components[adj_vertex] == 0:
                self.dfs_components(adj_vertex, current_component)

    def find_components(self):
        latest_component = 0
        for vertex in self.t_sort:
            if self.components[vertex] == 0:
                latest_component += 1
                self.dfs_components(vertex, latest_component)
        self.components_size = latest_component

    def find_edges_in_condensed_graph(self):
        edges = set()
        for vertex in range(self.size):
            component = self.components[vertex]
            for adj_vertex in self.graph[vertex]:
                adj_vertex_component = self.components[adj_vertex]
                if adj_vertex_component != component:
                    edges.add(frozenset([component, adj_vertex_component]))
        return len(edges)


def main():
    n, m = list(map(int, input().split()))

    g = Graph(n)

    for _ in range(m):
        v1, v2 = list(map(lambda x: int(x) - 1, input().split()))
        if v1 != v2:
            g.add_adjacent_vertex(v1, v2)

    g_rev = g.reverse()
    g.topological_sort()
    g_rev.t_sort = g.t_sort
    g_rev.find_components()
    print(g_rev.find_edges_in_condensed_graph())


if __name__ == '__main__':
    setrecursionlimit(10000)
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=main)
    thread.start()