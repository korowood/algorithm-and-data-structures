"""
Test1
input:
3 3 1
bbb
aba
baa

output:
aba
baa
bbb
_____________
Test2
input:
3 3 2
bbb
aba
baa

output:
baa
aba
bbb
_____________
"""


from itertools import accumulate


def sort_by_index(a, key_index):
    # символы конвертируются в числа от 65 до 122
    # можно использовать меньше памяти храня только 122-65 элементов в cnt
    # но я не буду, чтобы не загромождать код
    cnt = [0] * 123
    for s in a:
        cnt[s[key_index]] += 1

    prefix_sum = list(accumulate(cnt))

    output = [0] * n
    for elem in reversed(a):
        prefix_sum[elem[key_index]] -= 1
        position = prefix_sum[elem[key_index]]
        output[position] = elem
    return output


n, m, k = map(int, input().split())
a = []
for _ in range(n):
    s = input()
    s = [ord(c) for c in s]
    a.append(s)

for i in range(k):
    key = m - i - 1
    a = sort_by_index(a, key_index=key)

# переведем список интов в строки
a = [list(map(chr, x)) for x in a]
a = list(
    map(lambda x: ''.join(x), a)
)

print(*a, sep='\n')