"""
Реализуйте ассоциативный массив с использованием хеш таблицы.

input:
put hello privet
put bye poka
get hello
get bye
delete hello
get hello

output:
privet
poka
none
"""

import sys


class HashMap:
    def __init__(self):
        self.size = 10 ** 5
        self.P = 2004991
        self.A = 17
        self.data = [None] * self.size

    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash = (hash * self.A + ord(char)) % self.P
        return hash % self.size

    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.data[key_hash] is None:
            self.data[key_hash] = list([key_value])
            return True
        else:
            for pair in self.data[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.data[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.get_hash(key)
        if self.data[key_hash] is not None:
            for pair in self.data[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.get_hash(key)

        if self.data[key_hash] is None:
            return False
        for i in range(0, len(self.data[key_hash])):
            if self.data[key_hash][i][0] == key:
                self.data[key_hash].pop(i)
                return True


h = HashMap()

ans = []
for line in sys.stdin.buffer.read().decode().splitlines():
    arr = list(line.split())
    if arr[0][0] == 'p':
        h.add(arr[1], arr[2])
    elif arr[0][0] == 'd':
        h.delete(arr[1])
    else:
        # sys.stdout.write(h.get(arr[1]) + "\n")
        ans.append(h.get(arr[1]))

sys.stdout.buffer.write("\n".join(ans).encode())

for line in sys.stdin:
    st = line.split()
    if st[0] == 'put':
        h.add(st[1], st[2])
    elif st[0] == 'get':
        if h.get(st[1]) is None:
            print('none')
        else:
            print(h.get(st[1]))
    elif st[0] == 'delete':
        h.delete(st[1])
