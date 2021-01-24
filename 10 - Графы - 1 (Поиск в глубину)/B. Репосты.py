"""
______________
TEST1
input:
5
tourist reposted Polycarp
Petr reposted Tourist
WJMZBMR reposted Petr
sdya reposted wjmzbmr
vepifanov reposted sdya

output:
6
______________
TEST2
input:
6
Mike reposted Polycarp
Max reposted Polycarp
EveryOne reposted Polycarp
111 reposted Polycarp
VkCup reposted Polycarp
Codeforces reposted Polycarp

output:
2
_______________
TEST3
input:
1
SoMeStRaNgEgUe reposted PoLyCaRp

output:
2
"""

from sys import stdin
from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v):
        md = deque([[v, 0]])
        visit = defaultdict(int)
        visit[v] = 1
        level = defaultdict(int)
        while md:
            u, _level = md.pop()
            for i in self.graph[u]:
                if not visit[i]:
                    md.append([i, _level + 1])
                    visit[i], level[i] = 1, _level + 1

        return max(level.values()) + 1


g = Graph()
n = int(input())

for _ in range(n):
    b, rep, e = stdin.readline().lower().split()
    g.add(b, e)

ans = 0
for j in list(g.graph.keys()):
    ans = max(ans, g.dfs(j))

print(ans)
