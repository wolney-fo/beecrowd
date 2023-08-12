n = int(input())

for _ in range(n):
    a, b = map(str, input().split())

    if (a.endswith(b)):
        print('encaixa')
    else:
        print('nao encaixa')