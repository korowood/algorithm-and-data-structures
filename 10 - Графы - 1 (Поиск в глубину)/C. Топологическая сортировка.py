"""
Дан ориентированный невзвешенный граф. Необходимо построить его топологическую сортирвоку.
______________
TEST1
input:
6 6
1 2
3 2
4 2
2 5
6 5
4 6

output:
4 6 3 1 2 5
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
        self.ans = []
        self.color = defaultdict(int)
        self.flag = False

    def add(self, u_, v_):
        self.graph[u_].append(v_)

    def dfs(self, start):
        self.visited[start] = True
        for u in self.graph[start]:
            if not self.visited[u]:
                self.dfs(u)
        self.ans.append(start)

    def find_circle(self, start):
        self.color[start] = 1
        for u in self.graph[start]:
            if self.color[u] == 0:
                self.find_circle(u)
            if self.color[u] == 1:
                self.flag = True
                return
        self.color[start] = 2


def main():
    n, m = map(int, sys.stdin.buffer.readline().decode().split())
    g = Graph()

    for line in sys.stdin.buffer.read().decode().splitlines():
        b, e = map(int, line.split())
        g.add(b, e)

    for v in range(1, n + 1):
        if g.color[v] == 0 and not g.flag:
            g.find_circle(v)

    if g.flag:
        to_out = [-1]
    else:
        for v in range(1, n + 1):
            if not g.visited[v]:
                g.dfs(v)

        to_out = g.ans[::-1]
    sys.stdout.buffer.write(" ".join((map(str, to_out))).encode())


if __name__ == '__main__':
    threading.Thread(target=main).start()
