"""
input:
10
1 8 2 1 4 7 3 2 3 6

output:
1 1 2 2 3 3 4 6 7 8
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return
    middle = len(arr) // 2
    left = [arr[i] for i in range(0, middle)]
    right = [arr[i] for i in range(middle, len(arr))]
    merge_sort(left)
    merge_sort(right)
    i = k = n = 0
    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            arr[n] = left[i]
            i += 1
        else:
            arr[n] = right[k]
            k += 1
        n += 1

    while i < len(left):
        arr[n] = left[i]
        i += 1
        n += 1
    while k < len(right):
        arr[n] = right[k]
        k += 1
        n += 1
    return arr


t = int(input())
ml = list(map(int, input().split()))

print(*merge_sort(ml))
