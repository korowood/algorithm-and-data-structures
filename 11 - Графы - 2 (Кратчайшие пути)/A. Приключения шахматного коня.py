"""
На шахматной доске N×N в клетке (x1,y1) стоит голодный шахматный конь.
Он хочет попасть в клетку (x2,y2), где растет вкусная шахматная трава.
Какое наименьшее количество ходов он должен для этого сделать?
______________
input:
5
1 1
3 2

output:
2
1 1
3 2
"""

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start, distance, parents):
        distance[start] = 0
        queue = deque([start])

        while queue:
            cur_v = queue.popleft()
            for neight_v in self.graph[cur_v]:
                if distance[neight_v] is None:
                    distance[neight_v] = distance[cur_v] + 1
                    parents[neight_v] = cur_v
                    queue.append(neight_v)

    def get_edge(self, n):
        for i in range(n):
            for j in range(n):
                x1, y1 = i + 1, j + 1
                if 0 <= i + 2 < n and 0 <= j + 1 < n:
                    x2, y2 = i + 3, j + 2
                    self.graph[(x1, y1)].append((x2, y2))
                    self.graph[(x2, y2)].append((x1, y1))

                if 0 <= i - 2 < n and 0 <= j + 1 < n:
                    x2, y2 = i - 1, j + 2
                    self.graph[(x1, y1)].append((x2, y2))
                    self.graph[(x2, y2)].append((x1, y1))

                if 0 <= i + 1 < n and 0 <= j + 2 < n:
                    x2, y2 = i + 2, j + 3
                    self.graph[(x1, y1)].append((x2, y2))
                    self.graph[(x2, y2)].append((x1, y1))

                if 0 <= i - 1 < n and 0 <= j + 2 < n:
                    x2, y2 = i, j + 3
                    self.graph[(x1, y1)].append((x2, y2))
                    self.graph[(x2, y2)].append((x1, y1))


if __name__ == '__main__':
    N = int(input())

    g = Graph()
    g.get_edge(N)

    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    distance = {v: None for v in g.graph}
    parents = {v: None for v in g.graph}

    g.bfs(start, distance, parents)

    path = [end]
    parent = parents[end]
    while parent is not None:
        path.append(parent)
        parent = parents[parent]

    path = path[::-1]
    print(len(path))
    for x, y in path:
        print(x, y)
