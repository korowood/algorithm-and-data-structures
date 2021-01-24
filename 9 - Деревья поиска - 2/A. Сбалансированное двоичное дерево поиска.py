"""
Реализуйте сбалансированное двоичное дерево поиска.

input:
insert 2
insert 5
insert 3
exists 2
exists 4
next 4
prev 4
delete 5
next 4
prev 4

output:
true
false
5
3
none
3
"""

import sys

from random import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.prior = random()


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return 'false'

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return 'true'
        elif value < cur_node.value and cur_node.left is not None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._search(value, cur_node.right)
        return 'false'

    @staticmethod
    def next(root, value):
        res = None
        while root is not None:
            if root.value > value:
                res = root
                root = root.left
            else:
                root = root.right
        if res is None:
            return "none"
        return str(res.value)

    @staticmethod
    def prev(root, value):
        res = None
        while root is not None:
            if root.value < value:
                res = root
                root = root.right
            else:
                root = root.left
        if res is None:
            return "none"
        return str(res.value)

    def split(self, root, value):
        if root is None:
            return None, None
        elif root.value is None:
            return None, None
        else:
            if value < root.value:
                left, root.left = self.split(root.left, value)
                return left, root
            else:
                root.right, right = self.split(root.right, value)
                return root, right

    def merge(self, left, right):
        if (not left) or (not right):
            return left or right
        elif left.prior < right.prior:
            left.right = self.merge(left.right, right)
            return left
        else:
            right.left = self.merge(left, right.left)
            return right

    def insert(self, root, value: int):
        node = Node(value)
        left, right = self.split(root, value)
        return self.merge(self.merge(left, node), right)

    def delete(self, root, value: int):
        left, right = self.split(root, value - 1)
        _, right = self.split(right, value)
        return self.merge(left, right)


bst = BinarySearchTree()
ans = []

for line in sys.stdin:
    st = list(line.split())
    if st[0] == "insert":
        bst.root = bst.insert(bst.root, int(st[1]))
    elif st[0] == "delete":
        bst.root = bst.delete(bst.root, int(st[1]))
    elif st[0] == "exists":
        print(bst.search(int(st[1])))
    elif st[0] == "next":
        print(bst.next(bst.root, int(st[1])))
    elif st[0] == "prev":
        print(bst.prev(bst.root, int(st[1])))
