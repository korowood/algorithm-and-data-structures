"""
input:
4 11
802
743
457
539

output:
200
"""

from sys import stdin


def can_cut(length, k):
    i, it = k, iter(arr)
    cur_len = next(it)
    delta_i = cur_len // length
    while i > 0 and delta_i:
        i -= delta_i
        cur_len = next(it, 0)
        delta_i = cur_len // length
    return i <= 0


def max_len(arr, k):
    l, r = 0, arr[0] + 1
    while r - l != 1:
        mid = (r + l) // 2
        if can_cut(mid, k):
            l = mid
        else:
            r = mid
    return l


n, k = map(int, next(stdin).split())
arr = sorted((int(x) for x in stdin), reverse=True)
print(max_len(arr, k))
