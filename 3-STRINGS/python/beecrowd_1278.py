space = False

while True:
    n = int(input())

    if (n == 0):
        break

    maior = 0
    linhas = []

    for _ in range(n):
        inp = input().split()
        linha = ' '.join(inp)
        linhas.append(linha)
        if len(linha) > maior:
            maior = len(linha)

    if (space):
        print()
    else:
        space = True
    
    for l in linhas:
        print(" " * (maior - len(l)) + l)