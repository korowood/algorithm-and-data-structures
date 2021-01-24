"""
input:
5
1 2 3 4 5
sum 2 5
sum 1 5
sum 1 4
sum 2 4
set 1 10
set 2 3
set 5 2
sum 2 5
sum 1 5
sum 1 4
sum 2 4

output:
14
15
10
9
12
22
20
10
"""

import sys


class FenwickTree:
    def __init__(self, arr, n_):
        self.size = n_
        self.foo = [i_ & i_ + 1 for i_ in range(self.size)]
        self.t = [0 for _ in range(self.size)]
        self.data = arr

    def activate(self):
        for k in range(self.size):
            for j in range(self.foo[k], k + 1):
                self.t[k] += self.data[j]

    def set_elem(self, i_, x_):
        ind = i_ - 1
        d = x_ - self.data[ind]
        self.data[ind] = x_
        while ind < self.size:
            self.t[ind] += d
            ind = ind | (ind + 1)

    def get_sum(self, ind):
        res = 0
        index = ind - 1
        while index >= 0:
            res += self.t[index]
            index = self.foo[index] - 1
        return res

    def rsq(self, i_, x_):
        if i_ == 1:
            return FenwickTree.get_sum(self, x_)
        return FenwickTree.get_sum(self, x_) - FenwickTree.get_sum(self, i_ - 1)


n = int(sys.stdin.buffer.readline().decode())
a = list(map(int, sys.stdin.buffer.readline().decode().split()))

fenwick = FenwickTree(a, n)
fenwick.activate()
ans = []
for line in sys.stdin.buffer.read().decode().splitlines():
    op, i, x = list(line.split())
    if op == "set":
        fenwick.set_elem(int(i), int(x))
    else:
        ans.append(str(fenwick.rsq(int(i), int(x))))
sys.stdout.buffer.write("\n".join(ans).encode())


