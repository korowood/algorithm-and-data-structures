"""
Быстрая сортировка
input:
2
Louis IX
Louis VIII

output:
Louis VIII
Louis IX
_______________
input:
2
Louis IX
Philippe II

output:
Louis IX
Philippe II
"""


def solution(roman):
    md = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(roman) - 1):
        if md[roman[i]] < md[roman[i + 1]]:
            ans -= md[roman[i]]
        else:
            ans += md[roman[i]]
    ans += md[roman[len(roman) - 1]]
    return ans


ml = []
t = int(input())
for _ in range(t):
    name, titul = (map(str, input().split()))
    a = [name, titul, solution(titul)]
    ml.append(tuple(a))
ml.sort(key=lambda x: (x[0], x[2]))
for i in range(t):
    print(ml[i][0], ml[i][1], sep=' ')