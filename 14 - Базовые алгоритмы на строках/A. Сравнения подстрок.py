"""
Дана строка. Нужно уметь отвечать на запросы вида: равны ли подстроки [a..b] и [c..d].
_____________
TEST1
input:
trololo
3
1 7 1 7
3 5 5 7
1 1 1 5

output:
Yes
Yes
No
"""


class MyHashStr:
    def __init__(self):
        self.P = 31
        self.mod = 10 ** 9 + 7
        self.powp = [1]
        self.hash_arr = [0]

    def hash_str(self, s):
        self.hash_arr[0] = ord(s[0]) - ord("a") + 1
        for i in range(1, len(s)):
            x = ord(s[i]) - ord("a") + 1
            self.powp.append((self.powp[i - 1] * self.P) % self.mod)
            self.hash_arr.append((self.hash_arr[i - 1] * self.P + x) % self.mod)

    def get_hash(self, left, right):
        if left == 0:
            return self.hash_arr[right]
        return (self.hash_arr[right] - (
                self.hash_arr[left - 1] * self.powp[right - left + 1]) % self.mod + self.mod
                ) % self.mod


st = input()

mhs = MyHashStr()
mhs.hash_str(st)

m = int(input())
for j in range(m):
    a, b, c, d = map(int, input().split())

    hash_one = mhs.get_hash(a - 1, b - 1)
    hash_two = mhs.get_hash(c - 1, d - 1)

    print("Yes" if hash_one == hash_two else "No")
