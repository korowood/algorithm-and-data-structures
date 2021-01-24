"""
TEST1
input:
3 3 1 2 5 4

output:
YES
____________
TEST2
input:
4 2 4 2 4 5

output:
YES
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, point1, point2):
        self.x = point2.x - point1.x
        self.y = point2.y - point1.y


def dot_product(vector1, vector2):
    return vector1.x * vector2.x + vector1.y * vector2.y


def cross_product(vector1, vector2):
    return vector1.x * vector2.y - vector1.y * vector2.x


cx, cy, ax, ay, bx, by = map(int, input().split())
a_p, b_p, c_p = Point(ax, ay), Point(bx, by), Point(cx, cy)
ab = Vector(a_p, b_p)
ba = Vector(b_p, a_p)
ac = Vector(a_p, c_p)
bc = Vector(b_p, c_p)

cp_ab_ac = cross_product(ab, ac)
dp_ab_ac = dot_product(ab, ac)
dp_ba_bc = dot_product(ba, bc)
print("YES" if cp_ab_ac == 0 and dp_ab_ac >= 0 and dp_ba_bc >= 0 else "NO")
