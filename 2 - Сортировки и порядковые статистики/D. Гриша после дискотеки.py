"""
input:
4 3
aaab
aba

output:
8
____________
TEST2
input:
7 3
abacaba
abc


output:
15
"""

N_LETTERS = 26

n, m = map(int, input().split())
s = input()
cards = input()
cnt_cards = [0 for i in range(N_LETTERS)]
cnt_s = [[0] * N_LETTERS for i in range(n + 1)]
for i in range(m):
    cnt_cards[ord(cards[i]) - ord('a')] += 1
for i in range(1, n + 1):
    for j in range(N_LETTERS):
        cnt_s[i][j] = cnt_s[i - 1][j]
    cnt_s[i][ord(s[i - 1]) - ord('a')] += 1
left = 0
right = 1
ans = 0
while (right <= n):
    flag = True
    for i in range(N_LETTERS):
        if cnt_s[right][i] - cnt_s[left][i] > cnt_cards[i]:
            flag = False
            break
    if flag == True:
        ans += right - left
        right += 1
    else:
        left += 1
print(ans)
