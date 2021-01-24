"""
Выведите порядок элементов в массиве после выполнения всех операций.

input:
5 3
2 4
3 5
2 2

output:
1 4 5 2 3
"""

from sys import stdin, stdout
from random import randint

MAX_PRIORITY = 10 ** 9


class Node:
    def __init__(self, value, count, priority, left=None, right=None):
        self.value = value
        self.count = count
        self.priority = priority
        self.left = left
        self.right = right
        self.reversed = False


class CartesianTree:
    def __init__(self, root=None):
        self.root = root

    def get_count(self, v):
        if v is not None:
            return v.count
        else:
            return 0

    def fix_count(self, v):
        return self.get_count(v.left) + self.get_count(v.right) + 1

    def swap(self, v):
        tmp = v.left
        v.left = v.right
        v.right = tmp
        v.reversed = False
        if self.get_count(v.left) > 1:
            v.left.reversed = not v.left.reversed
        if self.get_count(v.right) > 1:
            v.right.reversed = not v.right.reversed
        return v

    def split(self, v, x):
        if v is None:
            return None, None
        if v.reversed:
            v = self.swap(v)
        if self.get_count(v.left) > x:
            tree_left, tree_right = self.split(v.left, x)
            v.left = tree_right
            v.count = self.fix_count(v)
            return tree_left, v
        else:
            tree_left, tree_right = self.split(v.right, x - self.get_count(v.left) - 1)
            v.right = tree_left
            v.count = self.fix_count(v)
            return v, tree_right

    def merge(self, tree_left, tree_right):
        if tree_left is None:
            return tree_right
        if tree_left.reversed:
            tree_left = self.swap(tree_left)
        if tree_right is None:
            return tree_left
        if tree_right.reversed:
            tree_right = self.swap(tree_right)
        if tree_left.priority > tree_right.priority:
            tree_left.right = self.merge(tree_left.right, tree_right)
            tree_left.count = self.fix_count(tree_left)
            if tree_left.reversed:
                tree_left = self.swap(tree_left)
            return tree_left
        else:
            tree_right.left = self.merge(tree_left, tree_right.left)
            tree_right.count = self.fix_count(tree_right)
            return tree_right

    def insert(self, v, value, ind, prior):
        tree_left, tree_right = self.split(v, ind)
        new_node = Node(value, 1, prior)
        tree_left = self.merge(tree_left, new_node)
        return self.merge(tree_left, tree_right)

    def reverse(self, v, left, right):
        tree_left, tree_right = self.split(v, right)
        tree_left_left, tree_left_right = self.split(tree_left, left - 1)
        if tree_left_right is not None and tree_left_right.reversed == False:
            tree_left_right = self.swap(tree_left_right)
        tree_left = self.merge(tree_left_left, tree_left_right)
        return self.merge(tree_left, tree_right)


n, m = map(int, stdin.buffer.readline().decode().strip().split())
my_tree = CartesianTree()
for i in range(n):
    my_tree = CartesianTree(my_tree.insert(my_tree.root, i + 1, i, randint(0, MAX_PRIORITY)))
for line in stdin.buffer.readlines():
    l, r = map(int, line.decode().strip().split())
    my_tree = CartesianTree(my_tree.reverse(my_tree.root, l - 1, r - 1))
lst = []
while True:
    t1, t2 = my_tree.split(my_tree.root, 0)
    my_tree = CartesianTree(root=t2)
    if t1 is not None:
        lst.append(str(t1.value))
    else:
        break
ans = ' '.join(lst)
stdout.buffer.write(ans.encode())
