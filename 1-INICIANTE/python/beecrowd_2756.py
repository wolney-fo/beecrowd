alf = 'ABCDE'
j = 0
x = -1

for i in range(6, 2, -1):
    print(' '*i, alf[j], end='')
    if x > 0:
        print((" "*x)+alf[j], end='')
    print()
    x += 2
    j += 1
for k in range(2, 7):
    print(' '*k, alf[j], end='')
    if x > 0:
        print((" "*x)+alf[j], end='')
    print()
    x -= 2
    j -= 1
