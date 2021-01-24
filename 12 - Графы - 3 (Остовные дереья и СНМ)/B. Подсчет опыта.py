"""
input:
3 6
add 1 100
join 1 3
add 1 50
get 1
get 2
get 3

output:
150
0
50
"""

import sys


class Game:
    def __init__(self, n_):
        self.rank = [0 for _ in range(n_)]
        self.prev = [i for i in range(n_)]
        self.next = [[] for _ in range(n_)]
        self.expirience = [0 for _ in range(n_)]

    def get(self, x):
        if self.prev[x] != x:
            self.prev[x] = self.get(self.prev[x])
        return self.prev[x]

    def join(self, x, y):
        x = self.get(x)
        y = self.get(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.prev[x] = y
        self.next[y].append(x)
        self.next[y] += self.next[x]

    def update_exp(self, x, v):
        point = self.get(x)
        self.expirience[point] += v
        for i in self.next[point]:
            self.expirience[i] += v


n, m = map(int, sys.stdin.buffer.readline().decode().split())

g = Game(n)

ans = []

for i in range(m):

    ml = list(input().split())
    if ml[0] == "join":
        g.join(int(ml[1]) - 1, int(ml[2]) - 1)
    elif ml[0] == "get":
        ans.append(str(g.expirience[int(ml[1]) - 1]))
    elif ml[0] == "add":
        g.update_exp(int(ml[1]) - 1, int(ml[2]))

for elem in ans:
    print(elem)


