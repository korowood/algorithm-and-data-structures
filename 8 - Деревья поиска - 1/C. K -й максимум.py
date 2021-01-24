"""
Напишите программу, реализующую структуру данных, позволяющую добавлять и удалять элементы,
а также находить k-й максимум.

input:
11
+1 5
+1 3
+1 7
0 1
0 2
0 3
-1 5
+1 10
0 1
0 2
0 3

output:
7
5
3
10
7
3
"""

import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.height = 0
        self.left = None
        self.right = None
        self.count = 0


class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, root, val):
        if root is None:
            return Node(val)
        elif val < root.value:
            root.left = self.insert(root.left, val)
        elif val > root.value:
            root.count += 1
            root.right = self.insert(root.right, val)
        return self.rebalanced(root)

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

    def delete(self, root, value):
        if root is None:
            return None
        elif root.value > value:
            root.left = self.delete(root.left, value)
        elif root.value < value:
            root.count -= 1
            root.right = self.delete(root.right, value)
        else:
            cur_value = root.left
            right_child = root.right
            if right_child is None:
                return cur_value
            min_node = self.find_root_min(right_child)
            min_node.count = root.count - 1
            min_node.right = self.delete_min(right_child)
            min_node.left = cur_value
            return self.rebalanced(min_node)
        return self.rebalanced(root)

    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def rebalanced(self, root):
        self.fix(root)
        if self.update_balance(root) == 2:
            if self.update_balance(root.right) < 0:
                root.right = self.r_rotate(root.right)
            return self.l_rotate(root)
        if self.update_balance(root) == -2:
            if self.update_balance(root.left) > 0:
                root.left = self.l_rotate(root.left)
            return self.r_rotate(root)
        return root

    def update_balance(self, root):
        return self.get_height(root.right) - self.get_height(root.left)

    def fix(self, root):
        a = self.get_height(root.left)
        b = self.get_height(root.right)
        root.height = max(a, b) + 1

    def r_rotate(self, root):
        cur_val = root.left
        root.left = cur_val.right
        cur_val.right = root
        cur_val.count += 1 + root.count
        self.fix(root)
        self.fix(cur_val)
        return cur_val

    def l_rotate(self, root):
        cur_val = root.right
        root.right = cur_val.left
        cur_val.left = root
        root.count -= (1 + cur_val.count)
        self.fix(root)
        self.fix(cur_val)
        return cur_val

    @staticmethod
    def find_root_min(root):
        while root.left is not None:
            root = root.left
        return root

    def delete_min(self, root):
        if root.left is None:
            return root.right
        root.left = self.delete_min(root.left)
        return self.rebalanced(root)

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

    def k_max(self, root, val):
        if root.count == val - 1:
            return str(root.value)
        elif root.count >= val:
            return self.k_max(root.right, val)
        else:
            return self.k_max(root.left, val - root.count - 1)


avl = AVLTree()
ans = []
n = int(sys.stdin.buffer.readline().decode())
for line in sys.stdin.buffer.read().decode().splitlines():
    y, x = list(line.split())
    if y[0] == '+':
        avl.root = avl.insert(avl.root, int(x))
    elif y[0] == "-":
        avl.root = avl.delete(avl.root, int(x))
    elif y[0] == "0":
        ans.append(avl.k_max(avl.root, int(x)))

sys.stdout.buffer.write("\n".join(ans).encode())
