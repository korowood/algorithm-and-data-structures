"""
Дан неориентированный граф, состоящий из N вершин и M ребер.
У каждого ребра которого есть маленькая пропускная способность. Между любой парой вершин может быть больше одного ребра.
Исток находится в вершине 1, а сток в вершине N. Требуется найти максимальный поток между истоком и стоком.
______________
input:
2
2
1 2 1
2 1 3

output:
4
"""

from math import inf


class Edge:
    def __init__(self, from_v, to_v, cap, dist):
        self.from_v = from_v
        self.to_v = to_v
        self.cap = cap
        self.dist = dist
        self.flow = 0


class Flow:
    def __init__(self, n):
        self.adj = [[] for _ in range(n)]

    def push_flow(self, v, t, cur_flow, used):
        used[v] = True
        if v == t:
            return cur_flow
        for edge in self.adj[v]:
            u = edge.to_v
            if not used[u] and edge.flow < edge.cap:
                next_flow = min(cur_flow, edge.cap - edge.flow)
                delta = self.push_flow(u, t, next_flow, used)
                if delta > 0:
                    edge.flow += delta
                    back_edge = self.adj[u][edge.dist]
                    back_edge.flow -= delta
                    return delta
        return 0


n = int(input())
m = int(input())

s, t = 0, n - 1
graph = Flow(n)
for i in range(m):
    a, b, c = (map(int, input().split()))
    edge = Edge(a - 1, b - 1, c, len(graph.adj[b - 1]))
    graph.adj[a - 1].append(edge)

    r_edge = Edge(b - 1, a - 1, c, len(graph.adj[a - 1]) - 1)
    graph.adj[b - 1].append(r_edge)

ans = 0

while True:
    used = [False for i in range(n)]
    delta = graph.push_flow(s, t, inf, used)
    if delta > 0:
        ans += delta
    else:
        break

print(ans)
