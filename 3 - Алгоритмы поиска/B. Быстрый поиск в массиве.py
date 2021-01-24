"""
Нужно уметь отвечать на запросы вида «Cколько чисел имеют значения от l до r»?

input:
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2

output:
5 2 2 0
"""

import sys


def lower_bound(arr, x):
    left = -1
    right = len(arr)
    while left < right - 1:
        mid = (right + left) // 2
        if x <= arr[mid]:
            right = mid
        else:
            left = mid
    return right


n = sys.stdin.readline()
ml = list(map(int, sys.stdin.readline().split()))
ml.sort()
k = sys.stdin.readline()
for _ in range(int(k)):
    left_b, right_b = map(int, sys.stdin.readline().split())
    a = lower_bound(ml, left_b)
    b = lower_bound(ml, right_b + 1)
    sys.stdout.write(str(b - a) + ' ')
