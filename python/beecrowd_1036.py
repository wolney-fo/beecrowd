from math import sqrt

a, b, c = map(float, input().split())

d = (b ** 2) - (4*a*c)
try:
    R1 = ( (b * (-1)) + sqrt(d) ) / (2*a)
    R2 = ( (b * (-1)) - sqrt(d) ) / (2*a)

    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))

except (ZeroDivisionError, ValueError):
    print('Impossivel calcular')

