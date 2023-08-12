               # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
letsPorNumero = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

n = int(input())

for _ in range(n):
    num = input()
    qtd = 0

    for dig in num:
        qtd += letsPorNumero[int(dig)]

    print(qtd, "leds")