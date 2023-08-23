t = int(input())

for _ in range(t):
    nomes = []
    prese = []
    exame = []

    n = int(input())
    nomes = input().split()
    prese = input().split()

    for i in range(n):
        presencas = prese[i].count('P')
        carga_hor = len(prese[i]) - prese[i].count('M')
        if presencas < carga_hor * 0.75:
            exame.append(nomes[i])
    
    print(' '.join(exame))
