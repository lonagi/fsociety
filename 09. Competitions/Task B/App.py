# OK

from itertools import combinations


def is_orth(a, b, c):
    return (b[0] - a[0]) * (b[0] - c[0]) + (b[1] - a[1]) * (b[1] - c[1]) == 0


def check_one(a, b, c, d):
    return is_orth(a, b, c) and is_orth(b, c, d) and is_orth(c, d, a)


def check(points):
    a, b, c, d = points
    return check_one(a, b, c, d) or check_one(b, c, a, d) or check_one(c, a, b, d)


N = int(input())
result = []
for test in range(N):

    K = int(input())
    points = set()
    for _ in range(K):
        xx, yy = list(map(int, input().split()))
        points.add((xx, yy))

    res = 0

    # for point1 in points:
    #     x1 = point1[0]
    #     y1 = point1[1]
    #     for point2 in points:
    #         if point2 != point1:
    #             x2, y2 = point2
    #             point3 = (x2, y1)
    #             point4 = (x1, y2)
    #             if point2!=point3 and point4 != point1:
    #                 if point3 in points and point4 in points:
    #                     res += 1
    #         else:
    #             continue
    for pair in combinations(points, 2):
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        if (x1, y2) in points and (x2, y1) in points and x1 != x2 and y1 != y2:
            # print(pair[0], pair[1], (x1, y2), (x2, y1))
            res += 1
    res = int(res/2)

    # for ps in combinations(points, 4):
    #     if check(ps):
    #         res += 1
    result.append(res)

for e in result:
    print(e)
