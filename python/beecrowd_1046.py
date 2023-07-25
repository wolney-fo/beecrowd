b, e = map(int, input().split())

if b > e:
    res = (24 - b) + e
elif b == e:
    res = 24
else:
    res = e - b

print('O JOGO DUROU {} HORA(S)'.format(res))
