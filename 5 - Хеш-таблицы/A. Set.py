"""
Реализуйте множество с использованием хеш таблицы.
input:
insert 2
insert 5
insert 3
exists 2
exists 4
insert 2
delete 2
exists 2

output:
true
false
false
"""

import sys


class HashSet:
    def __init__(self):
        self.M = 10 ** 6
        self.A = 4481
        self.P = 2004991
        self.data = ['' for _ in range(self.M)]

    def hash(self, key):
        return ((key * self.A) % self.P) % self.M

    def add(self, key):
        key_hash = self.hash(key)
        while not self.free(key_hash):
            if self.data[key_hash] == key:
                return
            key_hash = self.hash(key_hash + 1)
        self.data[key_hash] = key

    def exists(self, key):
        key_hash = self.hash(key)
        while not self.is_empty(key_hash):
            if self.data[key_hash] == key:
                return "true"
            else:
                key_hash = self.hash(key_hash + 1)
        return "false"

    def delete(self, key):
        key_hash = self.hash(key)
        while not self.is_empty(key_hash):
            if self.data[key_hash] == key:
                self.data[key_hash] = 'rip'
                break
            else:
                key_hash = self.hash(key_hash + 1)

    def free(self, x):
        if self.data[x] == '' or self.data[x] == 'rip':
            return True
        return False

    def is_empty(self, x):
        if self.data[x] == '':
            return True
        return False


hs = HashSet()
ans = []

for line in sys.stdin.buffer.read().decode().splitlines():
    arr = list(line.split())
    if arr[0][0] == "i":
        hs.add(int(arr[1]))
    elif arr[0][0] == 'd':
        hs.delete(int(arr[1]))
    elif arr[0][0] == 'e':
        ans.append(hs.exists(int(arr[1])))

sys.stdout.buffer.write("\n".join(ans).encode())
