"""
Реализуйте просто двоичное дерево поиска.

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


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            return value

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
        elif root.value < value:
            root.right = self.delete(root.right, value)
        elif root.value > value:
            root.left = self.delete(root.left, value)
        else:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                root.value = self.find_root(root.left).value
                root.left = self.delete(root.left, root.value)
        return root

    @staticmethod
    def find_root(root):
        while root.right is not None:
            root = root.right
        return root

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


bst = BinarySearchTree()
ans = []
for line in sys.stdin.buffer.read().decode().splitlines():
    st = list(line.split())
    if st[0] == "insert":
        bst.insert(int(st[1]))
    elif st[0] == "delete":
        bst.root = bst.delete(bst.root, int(st[1]))
    elif st[0] == "exists":
        ans.append(bst.search(int(st[1])))
    elif st[0] == "next":
        ans.append(bst.next(bst.root, int(st[1])))
    elif st[0] == "prev":
        ans.append(bst.prev(bst.root, int(st[1])))

sys.stdout.buffer.write("\n".join(ans).encode())
