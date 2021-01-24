"""
Необходимо проверить, пересекаются ли два отрезка.
input:
5 1 2 6
1 1 7 8

output:
YES
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def area(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


def intersect_1(a, b, c, d):
    if a > b:
        b, a = a, b
    if c > d:
        d, c = c, d
    return max(a, c) <= min(b, d)


def intersect_2(a, b, c, d):
    flag1 = intersect_1(a.x, b.x, c.x, d.x)
    flag2 = intersect_1(a.y, b.y, c.y, d.y)
    flag3 = area(a, b, c) * area(a, b, d) <= 0
    flag4 = area(c, d, a) * area(c, d, b) <= 0
    return flag1 and flag2 and flag3 and flag4


ax, ay, bx, by = map(int, input().split())
cx, cy, dx, dy = map(int, input().split())

a_p, b_p = Point(ax, ay), Point(bx, by)
c_p, d_p = Point(cx, cy), Point(dx, dy)

ans = intersect_2(a_p, b_p, c_p, d_p)
print("YES" if ans else "NO")
