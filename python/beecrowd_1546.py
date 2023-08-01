tab = ['Rolien', 'Naej', 'Elehcim', 'Odranoel']

_ = int(input())

for i in range(_):
    n = int(input())

    for j in range(n):
        inp = int(input())

        print(tab[inp-1])