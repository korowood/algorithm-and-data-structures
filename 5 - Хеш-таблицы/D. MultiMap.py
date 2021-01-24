"""
Реализуйте множественное отображение с использованием хеш таблиц.

input:
put a a
put a b
put a c
get a
delete a b
get a
deleteall a
get a

output:
3 a b c
2 a c
0
"""

from sys import stdin, stdout

MULTIMAP_CAPACITY = 10 ** 5
VALSET_CAPACITY = 2 ** 6

RIP = ''
EMPTY = None
SCALE = 4

P = 5454726281
A = 53
C = 10037


class Set:
    """
    Set на самописной Хеш-таблице с использованием открытой адресации
    Хэш-функция h(x) = (Ax % P) % M, где P - простое, A - случайное
    """

    def __init__(self, capacity):
        self._data = [(EMPTY, 0)] * capacity
        self._capacity = capacity
        self._ripped = 0
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        return iter(p[0] for p in self._data if p[0] != EMPTY and p[0] != RIP)

    def _items(self):
        return iter(p for p in self._data if p[0] != EMPTY and p[0] != RIP)

    def _hash(self, k):
        h = 0
        for c in k:
            h = (h * A + ord(c)) % P
        return h % self._capacity

    # инвариант хэш
    def _hash_part(self, k):
        h = 0
        for c in k:
            h = (h * A + ord(c)) % P
        return h

    def _rehash(self, data):
        for p in data:
            # инвариант хэш
            h = p[1] % self._capacity
            d = self._data[h][0]
            while d != EMPTY:
                h = (h + C) % self._capacity
                d = self._data[h][0]

            self._data[h] = p
            self._size += 1

    def _ensure_capacity(self, capacity):
        tmp = list(self._items())
        self._data = [(EMPTY, 0)] * capacity
        self._capacity = capacity
        self._ripped = 0
        self._size = 0

        self._rehash(tmp)

    def insert(self, x):
        if self._size + self._ripped >= self._capacity:
            self._ensure_capacity(self._size * SCALE)

        h1 = self._hash_part(x)
        h = h1 % self._capacity
        d = self._data[h][0]
        while d != EMPTY and d != x and d != RIP:
            h = (h + C) % self._capacity
            d = self._data[h][0]

        if d == EMPTY:
            self._data[h] = (x, h1)
            self._size += 1
            return

        if d == x:
            return

        if d == RIP:
            self._data[h] = (x, h1)
            self._ripped -= 1
            self._size += 1
            return

    def delete(self, x):
        h = self._hash(x)
        d = self._data[h][0]
        while d != EMPTY and d != x:
            h = (h + C) % self._capacity
            d = self._data[h][0]

        if d == x:
            self._data[h] = (RIP, 0)
            self._ripped += 1
            self._size -= 1

            if self._ripped > self._capacity // 2:
                self._ensure_capacity(self._size * SCALE)

    def get(self, x):
        h = self._hash(x)
        d = self._data[h][0]
        while d != EMPTY and d != x:
            h = (h + C) % self._capacity
            d = self._data[h][0]

        if d == x:
            return d
        return None


class MultiMap:
    """
    Мультиассоциативный массив с использованием хеш-таблицы
    Хэш-функция - полиномиальная с параметрами P - простое, A - простое
    """

    def __init__(self, capacity):
        self._data = [(EMPTY, 0, None)] * capacity
        self._capacity = capacity
        self._ripped = 0
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        return iter(x for x in self._data if x[0] != EMPTY and x[0] != RIP)

    def _hash(self, k):
        h = 0
        for c in k:
            h = (h * A + ord(c)) % P
        return h % self._capacity

    # инвариант хэш
    def _hash_part(self, k):
        h = 0
        for c in k:
            h = (h * A + ord(c)) % P
        return h

    def _rehash(self, data):
        for x in data:
            # инвариант хэш
            h = x[1] % self._capacity
            d = self._data[h][0]
            while d != EMPTY:
                h = (h + C) % self._capacity
                d = self._data[h][0]

            self._data[h] = x
            self._size += 1

    def _ensure_capacity(self, capacity):
        tmp = list(self)
        self._data = [(EMPTY, 0, None)] * capacity
        self._capacity = capacity
        self._ripped = 0
        self._size = 0

        self._rehash(tmp)

    def put(self, k, v):
        if self._size + self._ripped >= self._capacity:
            self._ensure_capacity(self._size * SCALE)

        h1 = self._hash_part(k)
        h = h1 % self._capacity

        d = self._data[h][0]
        while d != EMPTY and d != k and d != RIP:
            h = (h + C) % self._capacity
            d = self._data[h][0]

        if d == k:
            self._data[h][2].insert(v)
            return

        if d == EMPTY:
            valset = Set(VALSET_CAPACITY)
            valset.insert(v)
            self._data[h] = (k, h1, valset)
            self._size += 1
            return

        if d == RIP:
            valset = Set(VALSET_CAPACITY)
            valset.insert(v)
            self._data[h] = (k, h1, valset)
            self._ripped -= 1
            self._size += 1

    def delete(self, k, v):
        h = self._hash(k)
        d = self._data[h][0]
        while d != EMPTY and d != k:
            h = (h + C) % self._capacity
            d = self._data[h][0]

        if d == k:
            self._data[h][2].delete(v)
            self._ripped += 1
            self._size -= 1

    def delete_all(self, k):
        h = self._hash(k)
        d = self._data[h][0]
        while d != EMPTY and d != k:
            h = (h + C) % self._capacity
            d = self._data[h][0]

        if d == k:
            self._data[h] = (RIP, 0, None)
            self._ripped += 1
            self._size -= 1

    def get(self, k):
        h = self._hash(k)
        d = self._data[h][0]
        while d != EMPTY and d != k:
            h = (h + C) % self._capacity
            d = self._data[h][0]

        if d == k:
            valset = self._data[h][2]
            return str(len(valset)) + ' ' + ' '.join(valset)
        return '0'


q = stdin.buffer.read().decode().split()
a = []

m = MultiMap(MULTIMAP_CAPACITY)

i = 0
while i < len(q):
    cmd = q[i]
    k = q[i + 1]
    if cmd == 'put':
        m.put(k, q[i + 2])
        i += 3
    elif cmd == 'delete':
        m.delete(k, q[i + 2])
        i += 3
    elif cmd == 'deleteall':
        m.delete_all(k)
        i += 2
    elif cmd == 'get':
        a.append(m.get(k))
        i += 2

stdout.buffer.write('\n'.join(a).encode())
