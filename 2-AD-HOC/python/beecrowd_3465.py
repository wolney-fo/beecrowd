from math import sqrt

a, b, c = map(int, input().split())

s = (a + b + c) / 2
area = sqrt(s * (s - a) * (s - b) * (s - c))

print('{:.3f} m2'.format(area))