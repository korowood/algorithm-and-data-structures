"""
Дан неориентированный граф. Требуется выделить компоненты связности в нем.
______________
TEST1
input:
3 1
1 2

output:
2
1 1 2
______________
TEST2
input:
4 2
1 3
2 4

output:
2
1 2 1 2
"""

from collections import defaultdict
from sys import setrecursionlimit
import threading


class Graph:
    def __init__(self, size):
        self.graph = defaultdict(list)
        self.visited = [0] * (size + 1)

    def add(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start, vert):
        self.visited[start] = vert
        for u in self.graph[start]:
            if self.visited[u] == 0:
                self.dfs(u, vert)


def main():
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        b, e = map(int, input().split())
        g.add(b, e)
        g.add(e, b)

    for i in range(1, n + 1):
        if i not in g.graph.keys():
            g.add(i, i)

    cnt = 0
    for v in range(1, n + 1):
        if g.visited[v] == 0:
            cnt += 1
            g.dfs(v, cnt)

    print(cnt)
    print(*g.visited[1:])


setrecursionlimit(10 ** 9)
threading.stack_size(10 ** 8)
thread = threading.Thread(target=main)
thread.start()
