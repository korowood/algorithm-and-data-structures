"""
Даны строки p и t. Требуется найти все вхождения строки p в строку t в качестве подстроки.
input:
aba
abaCaba

output:
2
1 5
"""


def prefix_func(s, x):
    s_plus_x = x + '#' + s
    p = [0] * len(s_plus_x)
    for i in range(1, len(s_plus_x)):
        k = p[i - 1]
        while k > 0 and s_plus_x[k] != s_plus_x[i]:
            k = p[k - 1]
        if s_plus_x[k] == s_plus_x[i]:
            k += 1
        p[i] = k
    return p


st_1 = input()
st_2 = input()

prefix = prefix_func(st_2, st_1)
# print(prefix)
# ans = 0
ans = []
for j in range(len(prefix)):
    if prefix[j] == len(st_1):
        # ans += 1
        ans.append(j + 1 - 2 * len(st_1))

print(len(ans))
print(*ans)
