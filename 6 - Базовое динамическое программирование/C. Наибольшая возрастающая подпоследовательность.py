"""
Вам дана последовательность, содержащая n целых чисел. Найдите ее самую длинную возрастающую подпоследовательность.
____________________________________________
TEST 1
input:
8
1 4 1 5 3 3 4 2

output:
3
1 4 5
_____________________________________________
TEST 2
input:
3
1 2 3

output:
3
1 2 3
"""


def large_inc_seq(arr, n):
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and dp[j] > dp[i]:
                dp[i] = dp[j]
        dp[i] += 1

    final = max(dp)
    i = dp.index(final)
    ans = [arr[i]]

    while dp[i] != 1:
        j = i - 1
        while dp[j] + 1 != dp[i] or arr[j] >= arr[i]:
            j -= 1
        i = j
        ans.append(arr[i])
    return final, ans


k = int(input())
ml = list(map(int, input().split()))
large, massive = large_inc_seq(ml, k)
print(large)
print(' '.join(map(str, massive[::-1])))
