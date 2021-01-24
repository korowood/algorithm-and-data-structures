"""
Выведите порядок элементов в массиве после выполнения всех операций.

input:
6 3
2 4
3 5
2 2

output:
1 4 5 2 3 6
"""

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

    @staticmethod
    def get_size(root):
        return 0 if root is None else root.size

    def insert(self, root, value: int, x: int):
        node = Node(x)
        left, right = self.split(root, value)
        return self.merge(self.merge(left, node), right)

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

    def moving(self, l_, r_):
        left, right = self.split(self.root, l_ - 1)
        t1, t2 = self.split(right, r_ - l_)
        return self.merge(self.merge(t1, left), t2)


# n, m = map(int, sys.stdin.buffer.readline().decode().split())
n, m = map(int, input().split())
bst = BinarySearchTree()

for i in range(n):
    bst.root = bst.insert(bst.root, i, i + 1)
# for line in sys.stdin.buffer.read().decode().splitlines():
#     st = list(line.split())
#     bst.root = bst.moving(int(st[0]) - 1, int(st[1]) - 1)

for line in range(m):
    st = list(map(int, input().split()))
    bst.root = bst.moving(st[0] - 1, st[1] - 1)

bst.load_values()
print(" ".join(bst.arr))
