n = int(input())

for _ in range(n):
    inp = input()
    res = ''

    for letra in inp:
        res += chr(ord(letra) + 3) if letra.isalpha() else letra
    inp = res[::-1]
    inp = inp[:len(inp)//2] + ''.join([chr(ord(letra) - 1) for letra in inp[len(inp)//2:]])

    print(inp)