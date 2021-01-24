"""
input:
3 3
0 2 -3
2 -5 7
1 2 0

output:
6
RRDD
"""

n, m = [int(i) for i in input().split()]
apples = [[int(j) for j in input().split()] for i in range(n)]

dp = [[0 for j in range(m)] for i in range(n)]
path = []
dp[0][0] = apples[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j > 0:
            dp[i][j] = dp[i][j - 1] + apples[i][j]

        elif i > 0 and j == 0:
            dp[i][j] = dp[i - 1][j] + apples[i][j]

        elif i > 0 and j > 0:
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j] + apples[i][j]
            else:
                dp[i][j] = dp[i][j - 1] + apples[i][j]

while (i != 0) or (j != 0):
    if (i == 0) and (j > 0):
        j -= 1
        path.append('R')
        continue
    if (j == 0) and (i > 0):
        i -= 1
        path.append('D')
        continue
    if dp[i][j - 1] > dp[i - 1][j]:
        j -= 1
        path.append('R')
    else:
        i -= 1
        path.append('D')

print(dp[-1][-1])
print(*path[::-1], sep='')
