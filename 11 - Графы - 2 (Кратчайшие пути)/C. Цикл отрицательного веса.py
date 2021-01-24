"""
Дан ориентированный граф. Определите, есть ли в нем цикл отрицательного веса, и если да, то выведите его.
______________
input:
2
0 -1
-1 0

output:
YES
2
2 1
"""

from itertools import product
from math import inf

CONST = 100000


class Graph:
    def __init__(self):
        self.adj_matrix = []
        self.nxt = [[v for v in range(n)] for _ in range(n)]
        self.start = -1

    def update_dist(self):
        for i, j in product(range(n), repeat=2):
            if self.adj_matrix[i][j] == CONST:
                self.adj_matrix[i][j] = inf

    def floyd(self):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.adj_matrix[i][k] + self.adj_matrix[k][j] < self.adj_matrix[i][j]:
                        self.adj_matrix[i][j] = self.adj_matrix[i][k] + self.adj_matrix[k][j]
                        self.nxt[i][j] = self.nxt[i][k]
            for u in range(n):
                if self.adj_matrix[u][u] < 0:
                    self.start = u
                    break
            if self.start >= 0:
                break


def read_graph():
    g = Graph()

    g.adj_matrix = [list(map(int, input().split())) for _ in range(n)]

    g.update_dist()

    g.floyd()

    return g


def to_out(g):
    if not g.start >= 0:
        print("NO")
    else:

        u = g.start
        ans = []
        ans_set = set()
        while u not in ans_set:
            ans.append(u + 1)
            ans_set.add(u)
            u = g.nxt[u][g.start]
        print("YES", len(ans), sep='\n')
        for elem in ans:
            print(elem, end=' ')


if __name__ == '__main__':
    n = int(input())
    G = read_graph()
    to_out(G)
