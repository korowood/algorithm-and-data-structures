"""
input:
4
1 2 4 5

output:
0
"""


def merge_list(left, right):
    ans = list()
    i, j = 0, 0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
            count += (len(left) - i)
    ans += left[i:]
    ans += right[j:]
    return ans, count


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    middle = len(arr) // 2
    left, l_count = merge_sort(arr[:middle])
    right, r_count = merge_sort(arr[middle:])
    merged, count = merge_list(left, right)
    count += (l_count + r_count)
    return merged, count


t = int(input())
ml = list(map(int, input().split()))

print(merge_sort(ml)[1])