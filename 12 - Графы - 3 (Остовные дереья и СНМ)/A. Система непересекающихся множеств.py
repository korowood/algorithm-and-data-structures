"""
Реализуйте систему непересекающихся множеств. Вместе с каждым множеством храните минимальный,
максимальный элемент в этом множестве и их количество.
______________
input:
5
union 1 2
get 3
get 2
union 2 3
get 2
union 1 3
get 5
union 4 5
get 5
union 4 1
get 5

output:
3 3 1
1 2 2
1 3 3
5 5 1
4 5 2
1 5 5
"""

import sys


class NunIntersectSet:
    def __init__(self, min_elem_, max_elem_, cnt_):
        self.min_elem = min_elem_
        self.max_elem = max_elem_
        self.cnt = cnt_

    def get_property(self):
        return " ".join([str(self.min_elem + 1), str(self.max_elem + 1), str(self.cnt)])


def join(x, y):
    x = get_elem(x)
    y = get_elem(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[y] += 1
    prev[x] = y

    system[y].min_elem = min(system[y].min_elem, system[x].min_elem)
    system[y].max_elem = max(system[y].max_elem, system[x].max_elem)
    system[y].cnt += system[x].cnt


def get_elem(x):
    if prev[x] != x:
        prev[x] = get_elem(prev[x])
    return prev[x]


def load_system():
    # n = int(sys.stdin.buffer.readline().decode())
    n = int(input())

    rank_ = [0 for _ in range(n)]
    prev_ = [i for i in range(n)]
    system_ = [NunIntersectSet(i, i, 1) for i in range(n)]
    return rank_, prev_, system_


if __name__ == '__main__':
    rank, prev, system = load_system()
    # ans = []
    # for line in sys.stdin.buffer.read().decode().splitlines():
    for line in sys.stdin:
        ml = list(line.split())
        if ml[0] == "union":
            join(int(ml[1]) - 1, int(ml[2]) - 1)
        elif ml[0] == "get":
            point = get_elem(int(ml[1]) - 1)
            # ans.append(system[p].get_property())
            print(system[point].get_property())
    # sys.stdout.buffer.write("\n".join(ans).encode())
