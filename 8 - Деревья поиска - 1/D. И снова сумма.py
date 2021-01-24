"""
Реализуйте структуру данных, которая поддерживает множество S целых чисел,
с котором разрешается производить следующие операции:
    add(i) — добавить в множество S число i (если он там уже есть, то множество не меняется);
    sum(l,r) — вывести сумму всех элементов x из S, которые удовлетворяют неравенству l≤x≤r.

input:
6
+ 1
+ 3
+ 3
? 2 4
+ 1
? 2 4

output:
3
7
"""

import sys

CONST1 = pow(10, 9)


class Node:
    def __init__(self, k):
        self.key = k
        self.h = 0
        self.sum_under = 0
        self.balance = 0
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.overall_sum = 0

    def get_height(self, v):
        return 0 if v is None else v.h

    def get_key(self, v):
        return 0 if v is None else v.key

    def get_sum_under(self, v):
        return 0 if v is None else v.sum_under

    def get_balance(self, v):
        return self.get_height(v.right) - self.get_height(v.left)

    def fix(self, v):
        h1 = self.get_height(v.left)
        h2 = self.get_height(v.right)
        v.h = max(h1, h2) + 1

    def rotate_right(self, v):
        q = v.left
        tmp1 = self.get_key(v.right) + self.get_sum_under(v.right) + self.get_key(q.right) + self.get_sum_under(q.right)
        tmp2 = v.sum_under - q.key + v.key
        v.left = q.right
        q.right = v
        v.sum_under = tmp1
        q.sum_under = tmp2
        self.fix(v)
        self.fix(q)
        return q

    def rotate_left(self, v):
        p = v.right
        tmp1 = self.get_key(v.left) + self.get_sum_under(v.left) + self.get_key(p.left) + self.get_sum_under(p.left)
        tmp2 = v.sum_under - p.key + v.key
        v.right = p.left
        p.left = v
        v.sum_under = tmp1
        p.sum_under = tmp2
        self.fix(v)
        self.fix(p)
        return p

    def balance(self, v):
        self.fix(v)
        if self.get_balance(v) == 2:
            if self.get_balance(v.right) < 0:
                v.right = self.rotate_right(v.right)
            return self.rotate_left(v)
        if self.get_balance(v) == -2:
            if self.get_balance(v.left) > 0:
                v.left = self.rotate_left(v.left)
            return self.rotate_right(v)
        return v

    def exists(self, v, k):
        if v is None:
            return None
        elif v.key == k:
            return v
        elif v.key > k:
            return self.exists(v.left, k)
        else:
            return self.exists(v.right, k)

    def try_insertion(self, k):
        if self.exists(self.root, k) is None:
            self.root = self.insert(self.root, k)

    def insert(self, v, k):
        if v is None:
            self.overall_sum += k
            return Node(k)
        elif k < v.key:
            v.sum_under += k
            v.left = self.insert(v.left, k)
        elif k > v.key:
            v.sum_under += k
            v.right = self.insert(v.right, k)
        return self.balance(v)

    def get_sum(self, lower_bound, upper_bound):
        outside_sum1 = self.sum_to(self.root, lower_bound)
        outside_sum2 = self.sum_from(self.root, upper_bound)
        return self.overall_sum - outside_sum1 - outside_sum2

    def sum_to(self, v, lower_bound):
        if v is None:
            return 0
        elif v.key > lower_bound:
            return self.sum_to(v.left, lower_bound)
        elif v.key == lower_bound:
            return self.get_key(v.left) + self.get_sum_under(v.left)
        else:
            return self.get_key(v.left) + self.get_sum_under(v.left) + v.key + self.sum_to(v.right, lower_bound)

    def sum_from(self, v, upper_bound):
        if v is None:
            return 0
        elif v.key < upper_bound:
            return self.sum_from(v.right, upper_bound)
        elif v.key == upper_bound:
            return self.get_key(v.right) + self.get_sum_under(v.right)
        else:
            return self.get_key(v.right) + self.get_sum_under(v.right) + v.key + self.sum_from(v.left, upper_bound)


bt = BinaryTree()
ans = []
last_op = "+"
y = 0
n = int(sys.stdin.buffer.readline().decode())
for line in sys.stdin.buffer.read().decode().splitlines():
    a = list(line.split())
    if a[0] == "+":
        if last_op == "+":
            bt.try_insertion(int(a[1]))
        else:
            bt.try_insertion((int(a[1]) + y) % CONST1)
    elif a[0] == "?":
        y = bt.get_sum(int(a[1]), int(a[2]))
        ans.append(str(y))
    last_op = a[0]

sys.stdout.buffer.write("\n".join(ans).encode())
