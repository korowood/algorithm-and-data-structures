"""
TEST1
input:
5 5
--...
A-.#-
.#.#-
--.--
--.-B

output:
3
--+..
A-+#-
+#.#-
--.--
--.-B
____________
TEST2
input:
1 2
AB

output:
-1
"""

import sys
import threading
from collections import deque

INF = float('inf')


class Edge:
    __slots__ = ('to', 'reverse_edge', 'capacity', 'flow', 'x', 'y')

    def __init__(self, to, capacity, reverse_edge=-1, x=-1, y=-1):
        self.to = to
        self.reverse_edge = reverse_edge
        self.capacity = capacity
        self.flow = 0
        self.x = x
        self.y = y


class Node:
    __slots__ = ('depth', 'first_save_edge', 'edges')

    def __init__(self):
        self.depth = INF
        self.first_save_edge = 0
        self.edges = []


class FlowNetwork:
    def __init__(self, size):
        self.nodes = [Node() for _ in range(size)]
        self.sourse_idx = 0
        self.sink_idx = 0

    def add_edge(self, from_vertex, to_vertex, capacity):
        reverse_edge_idx_to = len(self.nodes[from_vertex].edges)
        reverse_edge_idx_from = len(self.nodes[to_vertex].edges)
        self.nodes[from_vertex].edges.append(Edge(to_vertex, capacity, reverse_edge_idx_from))
        self.nodes[to_vertex].edges.append(Edge(from_vertex, 0, reverse_edge_idx_to))

    def add_direct_edge(self, from_vertex, to_vertex, capacity, x, y):
        self.nodes[from_vertex].edges.append(Edge(to_vertex, capacity, x=x, y=y))

    def bfs_from_sourse(self):
        for node in self.nodes:
            node.depth = INF
            node.first_save_edge = 0

        self.nodes[self.sourse_idx].depth = 0
        queue = deque()
        queue.appendleft(self.sourse_idx)
        while queue:
            vertex = queue.pop()
            for edge in self.nodes[vertex].edges:
                if edge.flow < edge.capacity and self.nodes[edge.to].depth == INF:
                    self.nodes[edge.to].depth = self.nodes[vertex].depth + 1
                    queue.appendleft(edge.to)

        return self.nodes[self.sink_idx].depth != INF

    def find_block_flow(self, vertex, min_capacity):
        if vertex == self.sink_idx or min_capacity == 0:
            return min_capacity

        for edge_i in range(self.nodes[vertex].first_save_edge, len(self.nodes[vertex].edges)):
            edge = self.nodes[vertex].edges[edge_i]
            rev_edge = self.nodes[edge.to].edges[edge.reverse_edge]

            if self.nodes[edge.to].depth == self.nodes[vertex].depth + 1:
                delta = self.find_block_flow(edge.to, min(min_capacity, edge.capacity - edge.flow))
                if delta != 0:
                    edge.flow += delta
                    rev_edge.flow -= delta
                    return delta
            self.nodes[vertex].first_save_edge += 1
        return 0

    def find_max_flow(self):
        max_flow = 0

        while self.bfs_from_sourse():
            flow = self.find_block_flow(self.sourse_idx, INF)
            while flow != 0:
                max_flow += flow
                if max_flow >= INF:
                    return INF
                flow = self.find_block_flow(self.sourse_idx, INF)

        return max_flow


def main():
    n, m = map(int, input().split())

    network = FlowNetwork(10 ** 5)
    base_map = [['' for _ in range(m)] for _ in range(n)]

    def in_edge(i, j):
        return i * m + j

    def out_edge(i, j):
        return i * m + j + n * m

    for i, row in enumerate(sys.stdin.readlines()):
        for j, char in enumerate(row.strip()):
            base_map[i][j] = char
            if char == '-':
                network.add_direct_edge(in_edge(i, j), out_edge(i, j), INF, i, j)
            elif char == '.':
                network.add_direct_edge(in_edge(i, j), out_edge(i, j), 1, i, j)
            elif char == '#':
                network.add_direct_edge(in_edge(i, j), out_edge(i, j), 0, i, j)
            elif char == 'A':
                network.sourse_idx = out_edge(i, j)
            else:
                network.sink_idx = in_edge(i, j)

    for i in range(n - 1):
        for j in range(m - 1):
            network.add_edge(out_edge(i, j), in_edge(i + 1, j), INF)
            network.add_edge(out_edge(i + 1, j), in_edge(i, j), INF)
            network.add_edge(out_edge(i, j), in_edge(i, j + 1), INF)
            network.add_edge(out_edge(i, j + 1), in_edge(i, j), INF)

    for i in range(n - 1):
        network.add_edge(out_edge(i, m - 1), in_edge(i + 1, m - 1), INF)
        network.add_edge(out_edge(i + 1, m - 1), in_edge(i, m - 1), INF)

    for j in range(m - 1):
        network.add_edge(out_edge(n - 1, j), in_edge(n - 1, j + 1), INF)
        network.add_edge(out_edge(n - 1, j + 1), in_edge(n - 1, j), INF)

    max_flow = network.find_max_flow()
    if max_flow >= INF:
        print(-1)
    else:
        print(max_flow)

        visited = [False for _ in range(10 ** 5)]
        reach = []

        def dfs(v):
            visited[v] = True
            reach.append(v)

            for ed in network.nodes[v].edges:
                if not visited[ed.to] and ed.flow < ed.capacity:
                    dfs(ed.to)

        dfs(network.sourse_idx)
        for vertex in reach:
            for edge in network.nodes[vertex].edges:
                if not visited[edge.to] and edge.flow == 1:
                    base_map[edge.x][edge.y] = '+'

        for i in range(n):
            for j in range(m):
                print(base_map[i][j], end='')
            print()


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)  # лучше использовать именно эту константу
    thread = threading.Thread(target=main)
    thread.start()