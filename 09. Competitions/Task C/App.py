# OK

from fractions import Fraction
from math import comb



x = int(input())
result = []

for test in range(x):
    h = int(input())
    res = Fraction(0, 1)
    for i in range(h):
        level = list(map(int, input().split()))
        weight_sum = 0
        for j in range(i+1):
            # weight_sum += (binomial(i, j) * level[j])
            weight_sum += (int(comb(i, j)) * level[j])
        res += Fraction(weight_sum, 2 ** i)

    result.append(res)

for e in result:
    if e.numerator == 0:
        print('0', '1')
    else:
        print(e.numerator, e.denominator)

# 1
# 6
# 1
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1 -1
