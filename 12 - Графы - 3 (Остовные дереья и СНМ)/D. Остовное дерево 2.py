"""
Требуется в этом графе найти остовное дерево минимального веса.
______________
input:
4 4
1 2 1
2 3 2
3 4 5
4 1 4

output:
7
"""


class Edge:
    def __init__(self, prev=None, nxt=None, weight=None):
        self.prev = prev
        self.nxt = nxt
        self.weight = weight


class Graph:
    def __init__(self, n, m):
        self.edges = [None for _ in range(m)]
        self.rank = [0 for _ in range(n)]
        self.parent = [j for j in range(n)]

    def get(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.get(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        x, y = self.get(x), self.get(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.parent[x] = y


def create_grapg():
    n, m = (map(int, input().split()))

    graph = Graph(n, m)

    for i in range(m):
        x, y, w = map(int, input().split())
        graph.edges[i] = Edge(x - 1, y - 1, w)

    graph.edges.sort(key=lambda e: e.weight)
    return graph


if __name__ == '__main__':
    g = create_grapg()
    ans = 0

    for edge in g.edges:
        if g.get(edge.prev) != g.get(edge.nxt):
            ans += edge.weight
            g.join(edge.prev, edge.nxt)

    print(str(ans))
