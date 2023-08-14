isFirst = True

while True:
    n = int(input())

    if n == 0:
        break

    palavras = []
    maior = 0

    for _ in range(n):
        palavra = input()
        palavras.append(palavra)
        if len(palavra) > maior:
            maior = len(palavra)

    if isFirst:
        isFirst = False;
    else:
        print()

    
    for p in palavras:
        print(' ' * (maior - len(p)) + p)
