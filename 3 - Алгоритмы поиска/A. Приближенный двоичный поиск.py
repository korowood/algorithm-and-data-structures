"""
Для каждого запроса выведите число из первого массива наиболее близкое (то есть с минимальным модулем разности)
к числу в этом запросе. Если таких несколько, выведите меньшее из них.

input:
5 5
1 3 5 7 9
2 4 8 1 6

output:
1
3
7
1
5
"""


def bin_search(arr, x, step):
    left = 0
    right = len(arr) - 1
    for _ in range(step):
        middle = (right + left) // 2
        if arr[middle] < x:
            left = middle
        else:
            right = middle
    if x - arr[left] <= arr[right] - x:
        print(arr[left])
    else:
        print(arr[right])


STEPS = 100
n, k = map(int, input().split())
ml1 = list(map(int, input().split()))
ml2 = list(map(int, input().split()))
for i in range(k):
    (bin_search(ml1, ml2[i], STEPS))
