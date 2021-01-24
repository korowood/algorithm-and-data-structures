"""
Реализуйте прошитый ассоциативный массив с использованием хеш таблицы.

input:
put zero a
put one b
put two c
put three d
put four e
get two
prev two
next two
delete one
delete three
get two
prev two
next two
next four

output:
c
b
d
c
a
e
none
"""

import sys
from functools import reduce
from operator import attrgetter


class Node:
    def __init__(self, key, value=None, next_node=None, prev_node=None,
                 next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next_node
        self.prev = prev_node
        self.h_next = next
        self.h_prev = prev


class LinkedMap:

    def __init__(self):
        s = None
        self.len = 0
        self.A = 17
        self.P = 2004991
        self.hash_first = lambda x, y: (x * self.A + ord(y)) % self.P
        self.capacity = 10 ** 6
        self.data = [None] * self.capacity
        self.end = None

        if s is not None:
            for data in s:
                self[data[0]] = data[1]

    def __setitem__(self, key, value):
        i, node = self.index(key)
        if node is not None:
            node.value = value
        else:
            self.len += 1
            node = Node(key, value, self.data[i])
            if self.data[i] is not None:
                self.data[i].prev = node
            self.data[i] = node

            node.h_prev = self.end
            if self.end is not None:
                self.end.h_next = node
            self.end = node

    def hash_first(self, key):
        hash = 0
        for char in str(key):
            hash = (hash * self.A + ord(char)) % self.P
        return hash % self.size

    def hash(self, key):
        return reduce(self.hash_first, key, 0) % self.capacity

    def index(self, key):
        i = self.hash(key)
        node = self.data[i]
        while node is not None:
            if node.key == key:
                return i, node
            node = node.next
        return i, None

    def get(self, key, st):
        i, node = self.index(key)
        if node is not None:
            return node.value
        return st

    def delete(self, key):
        i, node = self.index(key)
        if node is not None:
            self.len -= 1
            _prev, _next = node.prev, node.next
            if _prev is None:
                self.data[i] = _next
            else:
                _prev.next = _next
            if _next is not None:
                _next.prev = _prev

            prev, next = node.h_prev, node.h_next
            if next is None:
                self.end = prev
            else:
                next.h_prev = prev
            if prev is not None:
                prev.h_next = next

    def find(self, key, op, st):
        i, node = self.index(key)
        if node is None:
            return st

        h_node = op(node)
        if h_node is not None:
            return h_node.value
        return st


lm = LinkedMap()
go_prev = attrgetter('h_prev')
go_next = attrgetter('h_next')

for line in sys.stdin:
    ml = list(line.split())
    if ml[0] == 'put':
        lm[ml[1]] = ml[2]
    elif ml[0] == 'delete':
        lm.delete(ml[1])
    elif ml[0] == 'get':
        sys.stdout.write(lm.get(ml[1], 'none'))
        sys.stdout.write('\n')
    elif ml[0] == 'prev':
        sys.stdout.write(lm.find(ml[1], go_prev, 'none'))
        sys.stdout.write('\n')
    elif ml[0] == 'next':
        sys.stdout.write(lm.find(ml[1], go_next, 'none'))
        sys.stdout.write('\n')
