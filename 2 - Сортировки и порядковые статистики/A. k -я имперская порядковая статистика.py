"""
input:
5
1 3 2 4 5
3
1 3 2
1 5 1
1 5 2

output:
2
1
2
"""


def find(arr, barrier):
    if len(arr) <= 1:
        return arr
    else:
        rand = (min(arr) + max(arr)) // 2
        left = [n for n in arr if n <= rand]
        right = [n for n in arr if n > rand]
        if barrier <= len(left):
            return find(left, barrier)
        else:
            return find(right, barrier - len(left))


n = int(input())
ml = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    i, j, k = map(int, input().split())
    ans = find(ml[i - 1: j], k)
    print(*ans)
