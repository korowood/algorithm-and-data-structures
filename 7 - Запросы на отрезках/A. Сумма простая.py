"""
Вам нужно научиться отвечать на запрос «сумма чисел на отрезке».
Массив не меняется. Запросов много. Отвечать на каждый запрос следует за O(1).

input:
3 1 2 3
3 1 -1 4

output:
23
"""

import sys


def simple_sum(n_, x_, y_, m_, z_, t_, b_0, a_0, const_1, const_2):
    a = [0 for _ in range(n_)]
    b = [0 for _ in range(2 * m_)]
    c = [0 for _ in range(2 * m_)]
    p_sum = [0 for _ in range(n_)]
    a[0] = a_0
    b[0] = b_0
    c[0] = b_0 % n_

    for i in range(1, n_):
        a[i] = (x_ * a[i - 1] + y_) % const_1
    for j in range(1, 2 * m_):
        b[j] = (z_ * b[j - 1] + t_) % const_2
        c[j] = b[j] % n_

    p_sum[0] = a[0]
    for k in range(1, n_):
        p_sum[k] = p_sum[k - 1] + a[k]

    ans = 0
    for j in range(m_):
        left = min(c[2 * j], c[2 * j + 1])
        right = max(c[2 * j], c[2 * j + 1])
        if left == 0:
            ans += p_sum[right]
        else:
            ans += p_sum[right] - p_sum[left - 1]
    return ans


N_len = 2 ** 16
M_len = 2 ** 30

n, x, y, a0 = list(map(int, sys.stdin.buffer.readline().decode().split()))
m, z, t, b0 = list(map(int, sys.stdin.buffer.readline().decode().split()))

to_out = simple_sum(n, x, y, m, z, t, b0, a0, N_len, M_len)
sys.stdout.buffer.write((str(to_out) + "\n").encode())
