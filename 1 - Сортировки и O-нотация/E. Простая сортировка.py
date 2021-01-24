"""
Быстрая сортировка
input:
10
1 8 2 1 4 7 3 2 3 6

output:
1 1 2 2 3 3 4 6 7 8
"""


from random import choice


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        rand = choice(arr)
        left = [n for n in arr if n < rand]
        middle = [rand] * arr.count(rand)
        right = [n for n in arr if n > rand]
        return quick_sort(left) + middle + quick_sort(right)


t = int(input())
ml = list(map(int, input().split()))
print(*quick_sort(ml))