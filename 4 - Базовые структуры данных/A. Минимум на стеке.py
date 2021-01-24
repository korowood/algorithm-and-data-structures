"""
Вам требуется реализовать структуру данных, выполняющую следующие операции:
    1. Добавить элемент x в конец структуры.
    2. Удалить последний элемент из структуры.
    3. Выдать минимальный элемент в структуре.

input:
8
1 2
1 3
1 -3
3
2
3
2
3

output:
-3
2
2
"""

import sys


class Node:
    def __init__(self, obj, next):
        self.obj = obj
        self.next = next

    def get_obj(self):
        return self.obj

    def get_next(self):
        return self.next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = Node(obj, self.top)
        else:
            ab = min(self.top.get_obj(), obj)
            self.top = Node(ab, self.top)

    def pop(self):
        if self.top is None:
            return None
        self.top = self.top.get_next()

    def get_min(self):
        return self.top.get_obj()


s = Stack()
n = sys.stdin.readline()
for _ in range(int(n)):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 1:
        s.push(a[1])
    elif a[0] == 2:
        s.pop()
    else:
        print(s.get_min())
