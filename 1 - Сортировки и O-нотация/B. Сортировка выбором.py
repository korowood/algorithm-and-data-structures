"""
input:
10
1 8 2 1 4 7 3 2 3 6

output:
1 1 2 2 3 3 4 6 7 8
"""


def choise_sort(arr):
    """ сортировка списка Аrr выбором"""
    n = len(arr)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if arr[k] < arr[pos]:
                arr[k], arr[pos] = arr[pos], arr[k]
    return arr


t = int(input())
ml = list(map(int, input().split()))
print(*choise_sort(ml))
