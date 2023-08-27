numeros = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

inp = input().strip()

try:
    print(numeros[int(inp)])
except:
    print(numeros.index(inp))