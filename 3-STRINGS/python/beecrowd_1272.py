n = int(input())

for _ in range(n):
    mensagem = ''
    palavras = [x.strip() for x in input().split()]

    for palavra in palavras:
        mensagem += palavra[0]

    print(mensagem)