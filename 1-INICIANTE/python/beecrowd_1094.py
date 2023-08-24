n = int(input())
cobaias = {
    'C': 0,
    'R': 0,
    'S': 0
}

for _ in range(n):
    q, t = input().split()
    cobaias[t] += int(q)

total = sum(cobaias.values())
coelhos = cobaias['C']
ratos = cobaias['R']
sapos = cobaias['S']

print('Total: {} cobaias'.format(total))
print('Total de coelhos:', coelhos)
print('Total de ratos:', ratos)
print('Total de sapos:', sapos)
print('Percentual de coelhos: {:.2f} %'.format((coelhos * 100) / total))
print('Percentual de ratos: {:.2f} %'.format((ratos * 100) / total))
print('Percentual de sapos: {:.2f} %'.format((sapos * 100) / total))
