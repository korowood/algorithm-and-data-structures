"""
input:
3 2 3
1 1
10 2
2 8

output:
YES
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point_coordinates_in_segment(self, a, b):
        return min(a.x, b.x) <= self.x <= max(a.x, b.x) and min(a.y, b.y) <= self.y <= max(a.y, b.y)


class Vector:
    def __init__(self, a: Point, b: Point):
        self.x = b.x - a.x
        self.y = b.y - a.y

    def cross_product(self, vector):
        res = self.x * vector.y - self.y * vector.x
        return res

    def scalar_product(self, vector):
        res = self.x * vector.x + self.y * vector.y
        return res

    def angle_between_vectors(self, vector):
        res = math.atan2(self.cross_product(vector), self.scalar_product(vector))
        return res


EPS = 10 ** (-9)
n, p_x, p_y = map(int, input().split())
p = Point(p_x, p_y)
on_edge = False

vertices = []
for i in range(n):
    x, y = map(int, input().split())
    vertices.append(Point(x, y))
vertices.append(vertices[0])

phi = 0
for i in range(n):
    pv_1 = Vector(p, vertices[i])
    pv_2 = Vector(p, vertices[i + 1])
    if pv_1.cross_product(pv_2) == 0 and p.point_coordinates_in_segment(vertices[i], vertices[i + 1]):
        on_edge = True
        break
    phi += pv_1.angle_between_vectors(pv_2)

if on_edge or (abs(phi) >= EPS):
    print('YES')
else:
    print('NO')