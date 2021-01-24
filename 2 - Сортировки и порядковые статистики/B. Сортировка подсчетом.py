"""
Дан список из N элементов, которые принимают целые значения от 0 до 100.
Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.
input:
7 3 4 2 5

output:
2 3 4 5 7
"""


def count_sort(arr):
    mx = max(arr)
    ans = [0 for _ in range(mx + 1)]
    for elem in arr:
        ans[elem] += 1
    i = 0
    for n in range(len(ans)):
        while ans[n] > 0:
            arr[i] = n
            i += 1
            ans[n] -= 1
    return arr


ml = list(map(int, input().split()))
print(*count_sort(ml))
