"""
input:
5 3
0.4

output:
0.783310604
"""

from math import sqrt


def foo(x, vel1, y):
    return sqrt(x ** 2 + (1 - y) ** 2) / vel1


def firewood(x, vel1, vel2, y):
    return foo(x, vel1, y) + foo(y, vel2, x)


vp, vf = map(int, input().split())
a = float(input())

left = 0
right = 1
step = 100

for _ in range(step):
    ground = left + (right - left) / 3
    forest = right - (right - left) / 3
    if firewood(ground, vp, vf, a) < firewood(forest, vp, vf, a):
        right = forest
    else:
        left = ground

print(left)
