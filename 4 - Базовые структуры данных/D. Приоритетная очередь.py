"""
Реализуйте приоритетную очередь. Ваша очередь должна поддерживать следующие операции: добавить элемент,
извлечь минимальный элемент, уменьшить элемент, добавленный во время одной из операций.

Если какой-нибудь decrease-key уменьшает уже удаленный элемент, то ничего делать не нужно.

Все операции нумеруются по порядку, начиная с 1.

input:
push 3
push 4
push 2
extract-min
decrease-key 2 1
extract-min
extract-min
extract-min

output:
2 3
1 2
3 1
*
"""

from sys import stdin, stdout
from math import inf


class Heap:
    def __init__(self):
        self._elements = []
        self.size = 0

    def __getitem__(self, item):
        return self._elements[item]

    def _swap(self, first_id, second_id):
        if first_id != second_id:
            help_list = self._elements[first_id]
            self._elements[first_id] = self._elements[second_id]
            self._elements[second_id] = help_list

    def insert(self, list_value):
        index = self.size
        self._elements.append(list_value)
        self.size += 1
        self._liftup(index)

    def _liftup(self, index):
        while index > 0:
            if self[index][0] < self[(index - 1) // 2][0]:
                self._swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def extract_min(self):
        if self.size == 0:
            return '*'
        minval = self[0]
        self._swap(0, self.size - 1)
        self.size -= 1
        self._elements.pop()
        index = 0
        while 2 * index + 1 < self.size:
            node = self[index][0]
            left = self[2 * index + 1][0]
            if 2 * index + 2 == self.size:
                right = inf
            else:
                right = self[2 * index + 2][0]
            if node > left:
                if left > right:
                    self._swap(index, 2 * index + 2)
                    index = 2 * index + 2
                    continue
                else:
                    self._swap(index, 2 * index + 1)
                    index = 2 * index + 1
                    continue
            if node > right:
                self._swap(index, 2 * index + 2)
                index = 2 * index + 2
                continue
            break
        return minval

    def decrease_key(self, index, value):
        for counter in range(self.size):
            if self[counter][1] == index:
                self[counter][0] = value
                self._liftup(counter)


array_heap = Heap()
counter = 0
for line in stdin:
    request = list(line.split())
    counter += 1
    if request[0] == 'push':
        array_heap.insert([int(request[1]), counter])
    if request[0] == 'extract-min':
        minval = array_heap.extract_min()
        if isinstance(minval, str):
            stdout.write(minval + '\n')
        else:
            stdout.write('{} {}\n'.format(minval[0], minval[1]))
    if request[0] == 'decrease-key':
        array_heap.decrease_key(int(request[1]), int(request[2]))
