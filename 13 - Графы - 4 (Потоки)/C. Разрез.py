"""
Найдите минимальный разрез между вершинами 1 и n в заданном неориентированном графе.
______________
input:
3 3
1 2 3
1 3 5
3 2 7

output:
2 8
1 2
"""

from math import inf

# INF = float('inf')


class Edge:
    def __init__(self, from_v, to_v, capacity, dist):
        self.from_v = from_v
        self.to_v = to_v
        self.capacity = capacity
        self.dist = dist
        self.flow = 0


class Graph:
    def __init__(self, n):
        self.size = n
        self.adj = [[] for _ in range(self.size)]
        self.edge_order = []
        self.cut_edges = []
        self.total_caps = 0

    def push(self, v, t, cur_flow, used):
        used[v] = True
        if v == t:
            return cur_flow
        for edge in self.adj[v]:
            u = edge.to_v
            if not used[u] and edge.flow < edge.capacity:
                next_flow = min(cur_flow, edge.capacity - edge.flow)
                delta = self.push(u, t, next_flow, used)
                if delta > 0:
                    edge.flow += delta
                    back_edge = self.adj[u][edge.dist]
                    back_edge.flow -= delta
                    return delta
        return 0

    def bfs(self):
        d = [-1 for _ in range(self.size)]
        d[s] = 0
        queue = [s]

        while queue:
            v = queue.pop(0)
            for edge in self.adj[v]:
                u = edge.to_v
                if edge.flow < edge.capacity and d[u] == -1:
                    d[u] = d[v] + 1
                    queue.append(u)
        return d[t] != -1

    def change(self, belongs_to_s, v):
        if belongs_to_s[v]:
            return
        belongs_to_s[v] = True
        for edge in self.adj[v]:
            if edge.flow != edge.capacity:
                self.change(belongs_to_s, edge.to_v)

    def restore(self):
        belongs_to_s = [False for _ in range(self.size)]
        self.change(belongs_to_s, s)
        i = 0
        for edge in self.edge_order:
            u = edge.from_v
            v = edge.to_v
            i += 1
            if belongs_to_s[u] == belongs_to_s[v]:
                continue
            self.cut_edges.append(str(i))
            self.total_caps += edge.capacity


def read_graph():
    n, m = map(int, input().split())

    g = Graph(n)
    for i in range(m):
        u, v, c = (map(int, input().split()))

        edge = Edge(u - 1, v - 1, c, len(g.adj[v - 1]))
        g.adj[u - 1].append(edge)

        r_edge = Edge(v - 1, u - 1, c, len(g.adj[u - 1]) - 1)
        g.adj[v - 1].append(r_edge)

        g.edge_order.append(g.adj[u - 1][-1])

    return g


if __name__ == '__main__':
    graph = read_graph()
    s, t = 0, graph.size - 1

    ans = 0
    while graph.bfs():
        used = [False for i in range(graph.size)]
        path = [None for i in range(graph.size)]
        delta = graph.push(s, t, inf, used)
        if delta > 0:
            ans += delta
        else:
            break

    graph.restore()
    print(len(graph.cut_edges), graph.total_caps)

    print(*graph.cut_edges)
