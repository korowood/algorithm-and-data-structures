"""
Научитесь быстро делать две операции с массивом:
    - add i x — добавить после i-го элемента x (0≤i≤n)
    - del i — удалить i-й элемент (1≤i≤n)

input:
3 4
1 2 3
del 3
add 0 9
add 3 8
del 2

output:
3
9 2 8
"""

import sys

from random import random


class Node:
    def __init__(self, x):
        self.x = x
        self.size = 1
        self.left = None
        self.right = None
        self.prior = random()


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.arr = []
        self.num = 0

    def split(self, root, value):
        if root is None:
            return None, None
        else:
            if self.get_size(root.left) > value:
                left, root.left = self.split(root.left, value)
                self.fix_size(root)
                return left, root
            else:
                root.right, right = self.split(root.right, value - self.get_size(root.left) - 1)
                self.fix_size(root)
                return root, right

    def merge(self, left, right):
        if (not left) or (not right):
            return left or right
        elif left.prior < right.prior:
            left.right = self.merge(left.right, right)
            self.fix_size(left)
            return left
        else:
            right.left = self.merge(left, right.left)
            self.fix_size(right)
            return right

    def fix_size(self, root):
        root.size = self.get_size(root.left) + self.get_size(root.right) + 1

    def get_size(self, root):
        return 0 if root is None else root.size

    def insert(self, root, value: int, x: int):
        node = Node(x)
        left, right = self.split(root, value)
        return self.merge(self.merge(left, node), right)

    def delete(self, root, value):
        left, right = self.split(root, value)
        t11, t12 = self.split(left, value - 1)
        left = self.merge(t11, right)
        return left

    def load_values(self):
        if self.root is not None:
            self.arr = [0 for _ in range(self.get_size(self.root))]
            self._load_values(self.root)

    def _load_values(self, root):
        if root is not None:
            if root.left is not None:
                self._load_values(root.left)
            self.arr[self.num] = str(root.x)
            self.num += 1
            self._load_values(root.right)


n, m = map(int, sys.stdin.buffer.readline().decode().split())
ml = list(map(int, sys.stdin.buffer.readline().decode().split()))

bst = BinarySearchTree()

for j in range(n):
    bst.root = bst.insert(bst.root, j, ml[j])
for line in sys.stdin.buffer.read().decode().splitlines():
    st = list(line.split())
    if st[0] == "add":
        bst.root = bst.insert(bst.root, int(st[1]) - 1, int(st[2]))
    elif st[0] == "del":
        bst.root = bst.delete(bst.root, int(st[1]) - 1)

print(bst.get_size(bst.root))
bst.load_values()
print(" ".join(bst.arr))
