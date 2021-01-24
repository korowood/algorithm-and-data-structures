"""
Определите расстояние Левенштейна для двух данных строк.

input:
ABCDEFGH
ACDEXGIH

output:
3
"""


def levenstein(arr_1, arr_2):
    n, m = len(arr_1), len(arr_2)
    if n > m:
        arr_1, arr_2 = arr_2, arr_1
        n, m = m, n

    dp = [i for i in range(n + 1)]
    for i in range(1, m + 1):
        prev, dp = dp, [i] + [0] * n

        for j in range(1, n + 1):
            add, delete, change = prev[j] + 1, dp[j - 1] + 1, prev[j - 1]
            if arr_1[j - 1] != arr_2[i - 1]:
                change += 1
            dp[j] = min(add, delete, change)

    return dp[n]


st1 = input()
st2 = input()
print(levenstein(st1, st2))
