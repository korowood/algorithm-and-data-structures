"""
input:
3
1 0
0 1
1 1

output:
0.5
"""

n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(float, input().split())))

ans = 0
for i in range(n):
    x1 = arr[i][0]
    y1 = arr[i][1]
    x2 = arr[(i + 1) % n][0]
    y2 = arr[(i + 1) % n][1]
    ans += x1 * y2 - x2 * y1

print(abs(ans) / 2)
