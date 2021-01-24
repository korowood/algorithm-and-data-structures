"""
Дан набор слов и текст, требуется определить для каждого слова, присутствует ли оно в тексте как подстрока.
input:
trololo
3
abacabadabacaba
olo
trol

output:
No
Yes
Yes
"""

from sys import stdin, stdout

MAX_WORD_LEN = 30


class Trie:
    def __init__(self):
        self.size = 1
        self.next = [dict()]
        self.terminal = [-1]

    def insert(self, s, n):
        v = 0
        for i in range(len(s)):
            if s[i] not in self.next[v].keys():
                self.next[v][s[i]] = self.size
                self.next.append(dict())
                self.terminal.append(-1)
                self.size += 1
            v = self.next[v][s[i]]
        self.terminal[v] = n

    def update(self, s):
        v = 0
        found_words = []
        for i in range(len(s)):
            if s[i] not in self.next[v].keys():
                return found_words
            if self.terminal[self.next[v][s[i]]] != -1:
                found_words.append(self.terminal[self.next[v][s[i]]])
            v = self.next[v][s[i]]
        return found_words


my_trie = Trie()
s = stdin.buffer.readline().decode().strip()
n = int(stdin.buffer.readline().decode().strip())
ans = ['No' for _ in range(n)]
for i in range(n):
    my_trie.insert(stdin.buffer.readline().decode().strip(), i)
for i in range(len(s)):
    to_update = my_trie.update(s[i:i + MAX_WORD_LEN])
    for ind in to_update:
        ans[ind] = 'Yes'
ans = '\n'.join(ans)
stdout.buffer.write(ans.encode())
