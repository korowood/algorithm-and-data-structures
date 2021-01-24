"""
TEST1
input:
4 1 1

output:
3
______________
TEST2
input:
5 1 2

output:
4
"""


def easy_task(i, j, k, step):
    minimum = min(j, k)
    if i == 1:
        return minimum
    else:
        left = 0
        right = (j + k + 1 - minimum) * i
        for _ in range(step):
            if right - left <= 1:
                return left + 1 + minimum
            middle = (right + left) // 2
            if i <= middle // j + middle // k + 1:
                right = middle
            else:
                left = middle


STEPS = 100
n, x, y = map(int, input().split())
print(easy_task(n, x, y, STEPS))
