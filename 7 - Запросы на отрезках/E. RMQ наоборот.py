"""
TEST 1
input:
3 2
1 2 1
2 3 2

output:
consistent
1 2 2
________________
TEST2
input:
3 3
1 2 1
1 1 2
2 3 2

output:
inconsistent
"""
from math import log2, ceil

MAX_POSSIBLE_VALUE = 2 ** 31 - 1


class STree:
    def __init__(self, n):
        self.pow_2 = ceil(log2(n))
        self.n_leaves = 2 ** self.pow_2
        self.min_tree = [MAX_POSSIBLE_VALUE] * (2 ** (self.pow_2 + 1) - 1)
        self.labels = [None] * len(self.min_tree)

    def push_labels(self, i, l_i, r_i):
        if r_i - l_i == 1 or self.labels[i] is None:
            return
        self.min_tree[2 * i + 1] = self.labels[i]
        self.min_tree[2 * i + 2] = self.labels[i]
        self.labels[2 * i + 1] = self.labels[i]
        self.labels[2 * i + 2] = self.labels[i]
        self.labels[i] = None

    def get_min(self, l, r, i, l_i, r_i):
        self.push_labels(i, l_i, r_i)

        if l >= r_i or l_i >= r:
            return MAX_POSSIBLE_VALUE
        elif l_i >= l and r_i <= r:
            return self.min_tree[i]

        m = (l_i + r_i) // 2
        ml = self.get_min(l, r, 2 * i + 1, l_i, m)
        mr = self.get_min(l, r, 2 * i + 2, m, r_i)

        return min(ml, mr)

    def set_x(self, l, r, i, x, l_i, r_i):
        self.push_labels(i, l_i, r_i)

        if l >= r_i or l_i >= r:
            return
        elif l_i >= l and r_i <= r:
            self.labels[i] = x
            self.min_tree[i] = x
            return

        m = (l_i + r_i) // 2
        self.set_x(l, r, 2 * i + 1, x, l_i, m)
        self.set_x(l, r, 2 * i + 2, x, m, r_i)
        self.min_tree[i] = min(self.min_tree[2 * i + 1], self.min_tree[2 * i + 2])


if __name__ == '__main__':
    queries = []

    with open('rmq.in') as in_f:
        n, m = map(int, in_f.readline().split())
        for line in in_f.readlines():
            i, j, q = map(int, line.split())
            queries.append((i, j, q))

    queries = sorted(queries, key=lambda x: x[2])
    t = STree(n)

    for i, j, q in queries:
        t.set_x(i - 1, j, 0, q, 0, t.n_leaves)

    status = None
    for i, j, q in queries:
        if t.get_min(i - 1, j, 0, 0, t.n_leaves) != q:
            status = 'inconsistent'
            break

    with open('rmq.out', 'w') as out_f:
        if status is not None:
            out_f.write(status)
        else:
            for i in range(2 ** t.pow_2 - 1):
                t.push_labels(i, 0, 2)

            res = t.min_tree[2 ** t.pow_2 - 1: 2 ** t.pow_2 + n - 1]
            out_f.write(f'consistent\n{" ".join(map(str, res))}')
