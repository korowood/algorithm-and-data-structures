"""
Для каждой операции изъятия элемента выведите ее результат.

На вход программе подаются строки, содержащие команды. Каждая строка содержит одну команду.
Команда — это либо "+ N", либо "-". Команда "+ N" означает добавление в очередь числа N, по модулю не превышающего 109.
Команда "-" означает изъятие элемента из очереди.

input:
4
+ 1
+ 10
-
-

output:
1
10
"""


class Stack:
    def __init__(self):
        self.n = 1
        self.data = [None] * self.n
        self.size = 0
        self.first = 0
        self.end = 0

    def push(self, val):
        self.grow()
        self.size += 1
        self.end = (self.end + 1) % self.n
        self.data[self.end] = val

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            first = self.data[self.first]
            self.first = (self.first + 1) % self.n
            self.down()
            return first

    def grow(self):
        if self.size == self.n:
            data_new = [None for _ in range(self.n * 2)]
            for i in range(self.size):
                data_new[i] = self.data[(self.first + i) % self.n]
            self.data = data_new
            self.n *= 2
            self.first = 0
            self.end = self.size - 1

    def down(self):
        if self.n <= 1:
            self.n = 1
            return
        if self.size <= (self.n // 2):
            data_new = [None for _ in range(self.n // 2)]
            for i in range(self.size):
                data_new[i] = self.data[(self.first + i) % self.n]
            self.data = data_new
            self.n //= 2
            self.first = 0
            self.end = self.size - 1


n = int(input())

s = Stack()
for _ in range(n):
    a = list(map(str, input().split()))
    if a[0] == '+':
        s.push(a[1])
    elif a[0] == '-':
        print(s.pop())
