"""
Дан массив из n чисел. Требуется написать программу, которая будет отвечать на запросы следующего вида:
найти минимум на отрезке между u и v включительно.

input:
10 8 12345
3 9

output:
5 3 1565158
"""

import sys

from math import log


class MyClass:
    def __init__(self, n_, a_0):
        self.size = n_
        self.lg = int(log(self.size, 2)) + 2
        self.dp = [[0 for _ in range(self.lg)] for _ in range(self.size)]
        self.mp = [0 for _ in range(self.size + 2)]
        self.a = [0 for _ in range(self.size)]
        self.a[0] = a_0

    def activate(self, c1, c2, c3):
        for i in range(1, self.size):
            self.a[i] = (c1 * self.a[i - 1] + c2) % c3

        for k in range(self.lg):
            for j in range(self.size):
                if k == 0:
                    self.dp[j][k] = self.a[j]
                else:
                    inx = min(j + 2 ** (k - 1), self.size - 1)
                    self.dp[j][k] = min(self.dp[j][k - 1], self.dp[inx][k - 1])

        for b in range(2, self.size + 2):
            self.mp[b] = self.mp[b - 1]
            if 1 << self.mp[b] < b:
                self.mp[b] += 1

        for t in range(self.size + 2):
            self.mp[t] -= 1

    def get_min(self, u_, v_):
        left = min(u_, v_) - 1
        right = max(u_, v_) - 1
        ix = self.mp[right - left + 2]
        ans = min(self.dp[left][ix], self.dp[right - 2 ** ix + 1][ix])
        return ans


n, m, a0 = list(map(int, sys.stdin.buffer.readline().decode().split()))
u, v = list(map(int, sys.stdin.buffer.readline().decode().split()))
ms = MyClass(n, a0)

Const1_a, Const2_a, Const3_a = 23, 21563, 16714589
Const1_u, Const2_u, Const3_u = 17, 751, 2
Const1_v, Const2_v, Const3_v = 13, 593, 5
ms.activate(Const1_a, Const2_a, Const3_a)

r = ms.get_min(u, v)
for q in range(1, m):
    u = ((Const1_u * u + Const2_u + r + Const3_u * q) % n) + 1
    v = ((Const1_v * v + Const2_v + r + Const3_v * q) % n) + 1
    r = ms.get_min(u, v)

sys.stdout.buffer.write((str(u) + " " + str(v) + " " + str(r) + "\n").encode())
