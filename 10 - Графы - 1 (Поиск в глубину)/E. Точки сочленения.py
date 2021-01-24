"""
Дан неориентированный граф. Требуется найти все точки сочленения в нём.
______________
TEST1
input:
6 7
1 2
2 3
2 4
2 5
4 5
1 3
3 6

output:
2
2 3
"""

from collections import defaultdict
import sys
import threading

sys.setrecursionlimit(10 ** 9)
threading.stack_size(10 ** 8)


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = defaultdict(bool)
        self.up = defaultdict(int)
        self.time_in = defaultdict(int)
        self.time = 0
        self.articulation_points = set()

    def add(self, u_, v_):
        self.graph[u_].append(v_)

    def dfs(self, start, point):
        self.time += 1
        self.time_in[start] = self.time
        self.up[start] = self.time
        self.visited[start] = True
        cnt = 0
        for u in self.graph[start]:
            if u == point:
                continue
            if self.visited[u]:
                self.up[start] = min(self.up[start], self.time_in[u])
            else:
                self.dfs(u, start)
                cnt += 1
                self.up[start] = min(self.up[start], self.up[u])
                if point != -1 and self.up[u] >= self.time_in[start]:
                    self.articulation_points.add(start)
        if point == -1 and cnt >= 2:
            self.articulation_points.add(start)


def main():
    n, m = map(int, input().split())
    g = Graph()

    for _ in range(m):
        b, e = map(int, input().split())
        g.add(b, e)
        g.add(e, b)

    for v in range(1, n + 1):
        if not g.visited[v]:
            g.dfs(v, -1)

    print(len(g.articulation_points))
    print(*sorted(list(g.articulation_points)))


threading.Thread(target=main).start()
