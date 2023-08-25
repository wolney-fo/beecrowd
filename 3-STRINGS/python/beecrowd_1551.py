n = int(input())

ALFABETO = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(n):
    letras_usadas = []

    frase = input().strip().replace(' ', '').replace(',', '')

    for letra in frase:
        if not letra in letras_usadas:
            letras_usadas.append(letra)

    if len(letras_usadas) == 26:
        print('frase completa')
    elif len(letras_usadas) >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')