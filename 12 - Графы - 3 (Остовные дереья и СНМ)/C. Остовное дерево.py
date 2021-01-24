"""
Требуется в этом графе найти остовное дерево минимального веса.
______________
input:
2
0 0
1 1

output:
1.4142135624
"""

from math import sqrt


class Graph:
    INF = (1 << 32) - 1

    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.__points = []
        self.__dist = [self.INF] * n_vertices
        self.__used = set()

    def add_point(self, begin, end):
        self.__points.append([begin, end])

    def prim(self):
        ans = 0
        self.__dist[0] = 0
        for i in range(self.n_vertices):
            min_dist = self.INF
            for j in range(self.n_vertices):
                if j not in self.__used and self.__dist[j] < min_dist:
                    min_dist = self.__dist[j]
                    u = j
            ans += min_dist
            self.__used.add(u)
            for j in range(self.n_vertices):
                self.__dist[j] = min(self.__dist[j], self.distance(u, j))
        return ans

    def distance(self, begin, end):
        x0, y0 = self.__points[begin]
        x1, y1 = self.__points[end]
        return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)


def main():
    n_vertices = int(input())
    g = Graph(n_vertices)
    for _ in range(n_vertices):
        begin, end = [int(x) for x in input().split()]
        g.add_point(begin, end)
    print(g.prim())


if __name__ == '__main__':
    main()
