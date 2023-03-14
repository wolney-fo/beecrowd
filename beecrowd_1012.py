values = list(map(float, input().split()))

print('TRIANGULO: {:.3f}'.format((values[0] * values[2]) / 2))
print('CIRCULO: {:.3f}'.format((3.14159 * values[2] ** 2.0)))
print('TRAPEZIO: {:.3f}'.format(((values[0] + values[1]) * values[2]) / 2))
print('QUADRADO: {:.3f}'.format(values[1] ** 2.0))
print('RETANGULO: {:.3f}'.format(values[0] * values[1]))