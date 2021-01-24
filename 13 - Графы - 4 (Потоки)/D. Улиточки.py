"""
input:
3 3 1 3
1 2
1 3
2 3

output:
YES
1 3
1 2 3
"""

import sys
import threading
from math import inf

sys.setrecursionlimit(10 ** 9)
threading.stack_size(10 ** 8)


def solve():
    class Edge:
        def __init__(self, from_v, to_v, capacity, dist):
            self.from_v = from_v
            self.to_v = to_v
            self.capacity = capacity
            self.dist = dist
            self.flow = 0

    class Graph:
        def __init__(self):
            self.adj = [[] for _ in range(n)]

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

        def restore(self, path, from_v, to_v):
            path.append(str(from_v + 1))
            if from_v == to_v:
                return
            for edge in self.adj[from_v]:
                if edge.flow != edge.capacity or edge.capacity == 0:
                    continue
                else:
                    edge.flow = 0
                    self.adj[edge.to_v][edge.dist].flow = 0
                    self.restore(path, edge.to_v, to_v)
                    break

    n, m, s, t = map(int, input().split())

    g = Graph()
    for i in range(m):
        u, v = map(int, input().split())
        edge = Edge(u - 1, v - 1, 1, len(g.adj[v - 1]))
        g.adj[u - 1].append(edge)

        r_edge = Edge(v - 1, u - 1, 0, len(g.adj[u - 1]) - 1)
        g.adj[v - 1].append(r_edge)

    s -= 1
    t -= 1
    ans = 0
    while True:
        used = [False for _ in range(n)]
        delta = g.push(s, t, inf, used)
        if delta > 0:
            ans += delta
        else:
            break

    if ans < 2:
        # sys.stdout.buffer.write("NO\n".encode())
        print("NO")
    else:
        ans_1, ans_2 = [], []
        g.restore(ans_1, s, t)
        g.restore(ans_2, s, t)
        if len(ans_1) > len(ans_2):
            # ans_1, ans_2 = ans_2, ans_1
            print("YES")
            print(*ans_2)
            print(*ans_1)
        else:
            print("YES")
            print(*ans_1)
            print(*ans_2)


def main():
    solve()


if __name__ == "__main__":
    threading.Thread(target=main).start()
