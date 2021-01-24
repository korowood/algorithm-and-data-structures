"""
____________________________________________
TEST 1
input:
5
110
40
120
110
60

output:
260
0 2
3
5
_____________________________________________
TEST 2
input:
3
110
110
110

output:
220
1 1
2
"""

from math import inf

MIN_PRICE = 100

n = int(input())
dp = [[0 for i in range(n + 3)] for j in range(n + 1)]
prev = [[None for i in range(n + 3)] for j in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = inf
    dp[i][n + 2] = inf
for j in range(2, n + 3):
    dp[0][j] = inf
for i in range(1, n + 1):
    price = int(input())
    for j in range(n + 1, 0, -1):
        if price <= MIN_PRICE:
            if dp[i - 1][j] + price < dp[i - 1][j + 1]:
                dp[i][j] = dp[i - 1][j] + price
                prev[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j + 1]
                prev[i][j] = -1
        else:
            if dp[i - 1][j - 1] + price < dp[i - 1][j + 1]:
                dp[i][j] = dp[i - 1][j - 1] + price
                prev[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j + 1]
                prev[i][j] = -1
min_sum = dp[n][n + 2]
left_coupons = n + 2
for j in range(n + 1, 0, -1):
    if dp[n][j] < min_sum:
        min_sum = dp[n][j]
        left_coupons = j - 1
print(min_sum)
paid_coupons = []
n_coup = left_coupons
for i in range(n, 0, -1):
    if prev[i][n_coup + 1] == 1:
        n_coup -= 1
    elif prev[i][n_coup + 1] == -1:
        n_coup += 1
        paid_coupons.append(i)
print(left_coupons, len(paid_coupons))
paid_coupons.reverse()
for k in range(len(paid_coupons)):
    print(paid_coupons[k])
