"""
Даны K строк из маленьких латинских букв. Требуется найти их наибольшую общую подстроку.
input:
3
abacaba
mycabarchive
acabistrue

output:
cab
"""

from collections import defaultdict

DEFAULT_MULT = 31
DEFAULT_MOD = 1073676287


class HashString:
    def __init__(self, string, p=DEFAULT_MULT, m=DEFAULT_MOD):
        self.string = string
        self.p = p
        self.m = m
        self.hashes = []
        self.powers = []
        self.prepare_hashes()

    def prepare_hashes(self):
        cur_hash = 0
        cur_p = 1
        for char in self.string:
            cur_hash = cur_hash * self.p + ord(char)
            cur_hash %= self.m
            self.hashes.append(cur_hash)
            self.powers.append(cur_p)
            cur_p = (cur_p * self.p) % self.m

    def compute_hash(self, a, b):
        if a == 0:
            return self.hashes[b]
        return (self.hashes[b] - self.hashes[a - 1] * self.powers[b - a + 1]) % self.m

    def __len__(self):
        return len(self.string)


def exists_lcp(words, cur_len):
    hashes = defaultdict(list)
    intersected_hashes = set()
    for idx, word in enumerate(words):
        for i in range(len(word) - cur_len + 1):
            hashes[word].append(word.compute_hash(i, i + cur_len - 1))
        if idx == 0:
            intersected_hashes = set(hashes[word])
        else:
            intersected_hashes = intersected_hashes.intersection(set(hashes[word]))
            if len(intersected_hashes) == 0:
                return False, []

    for i in range(len(hashes[word])):
        if hashes[word][i] in intersected_hashes:
            return True, word.string[i:i + cur_len]


def get_lcp(words):
    # for fast breaking loop in exists_lcp
    words = list(map(HashString, sorted(words, key=len)))
    min_len = len(words[0])

    left, right = 1, min_len + 1
    best_lcp = None
    while left < right:
        middle = (right + left) // 2
        exists, res = exists_lcp(words, middle)
        if not exists:
            right = middle
        else:
            best_lcp = res
            left = middle + 1
    return best_lcp


if __name__ == '__main__':
    k = int(input())
    words = []
    for _ in range(k):
        words.append(input())

    print(get_lcp(words))