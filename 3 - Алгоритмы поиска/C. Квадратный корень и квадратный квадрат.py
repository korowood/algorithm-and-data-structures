"""
TEST1
input:
2.0000000000

output:
1.0
______________
TEST2
input:
18.0000000000

output:
4.0
"""

from math import sqrt


def find_const(x, left, right, eps, steps):
    for _ in range(steps):
        middle = (left + right) / 2
        if right - left < eps:
            return right
        if middle * middle + sqrt(middle) >= x:
            right = middle
        else:
            left = middle


EPS = 10e-6
STEPS = 100
RIGHT_BOARD = 1e10
LEFT_BOARD = 0.0
num = float(input())
print(round(find_const(num, LEFT_BOARD, RIGHT_BOARD, EPS, STEPS), 6))
