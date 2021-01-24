"""
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов.
Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D,
а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и
дополнительных соглашений о приоритете операторов для своего чтения.

Дано выражение в обратной польской записи. Определите его значение.

input:
8 9 + 1 7 - *

output:
-102
"""

import sys


class Stack:
    def __init__(self):
        self.n = 1
        self.data = [None] * self.n
        self.size = 0

    def push(self, val):
        self.grow()
        stack_size = self.size
        self.data[stack_size] = val
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            last = self.data[self.size]
            self.data[self.size] = None
            self.down()
            return last

    def grow(self):
        if self.size == self.n:
            double_n = [None] * self.n
            self.data = self.data + double_n
            self.n = self.n * 2

    def down(self):
        if self.n <= 2:
            self.n = 2
            return
        if self.size <= (self.n // 2):
            self.data = self.data[:self.size]
            self.n = self.n // 2


def postfix(arr):
    s = Stack()

    for elem in arr:
        if elem in "0123456789":
            s.push(int(elem))
        else:
            operand_2 = s.pop()
            operand_1 = s.pop()
            result = math_operation(elem, operand_1, operand_2)
            s.push(result)
    return s.pop()


def math_operation(el, op_1, op_2):
    if el == "*":
        return op_1 * op_2
    elif el == "/":
        return op_1 / op_2
    elif el == "+":
        return op_1 + op_2
    else:
        return op_1 - op_2


ml = list(map(str, sys.stdin.readline().split()))
print(postfix(ml))
