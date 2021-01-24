"""
Нужно вычислить периметр выпуклой оболочки данных точек.
input:
5
0 0
2 0
0 2
1 1
2 2

output:
8
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x or ((self.x == other.x) and self.y < other.y)


class Vector:
    def __init__(self, a: Point, b: Point):
        self.x = b.x - a.x
        self.y = b.y - a.y

    def cross_product(self, vector):
        res = self.x * vector.y - self.y * vector.x
        return res

    def length(self):
        return (math.sqrt(self.x ** 2 + self.y ** 2))


def slope(point):
    p_0 = points[0]
    if p_0.x != point.x:
        return (p_0.y - point.y) / (p_0.x - point.x)
    return math.inf


def sort_points(points):
    points.sort()
    point_array = points[:1] + sorted(points[1:], key=slope)
    return point_array


def graham_scan(points):
    convex_hull = []
    sorted_points = sort_points(points)
    for point in sorted_points:
        while len(convex_hull) >= 2 and Vector(convex_hull[-1], convex_hull[-2]).cross_product(
                Vector(convex_hull[-1], point)) >= 0:
            convex_hull.pop()
        convex_hull.append(point)
    convex_hull.append(convex_hull[0])
    return convex_hull


n = int(input())
used = [False] * n
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

convex_hull = graham_scan(points)
perimeter = 0
for i in range(len(convex_hull) - 1):
    perimeter += Vector(convex_hull[i], convex_hull[i + 1]).length()

print(perimeter)
