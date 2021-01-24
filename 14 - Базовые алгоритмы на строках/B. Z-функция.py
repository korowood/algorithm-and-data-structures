"""
Постройте Z-функцию для заданной строки s.
_____________
TEST1
input:
aaaAAA

output:
2 1 0 0 0
_____________
TEST2
input:
abacaba

output:
 0 1 0 3 0 1
"""


def z_func(s):
    n = len(s)
    z = [0] * n
    left, right = 0, 0

    for i in range(1, n):
        if right >= i:
            z[i] = min(z[i - left], right - i + 1)

        while z[i] + i < n and s[z[i]] == s[z[i] + i]:
            z[i] += 1

        if z[i] + i - 1 > right:
            left = i
            right = z[i] + i - 1
    return z


if __name__ == "__main__":
    st = input()
    print(*z_func(st)[1:])
