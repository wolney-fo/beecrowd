n = int(input())

for _ in range(n):
    counter = 0 

    t = int(input())
    tiros = [int(x) for x in input().split()]
    pulos = input()

    for j in range(t):
        if (tiros[j] <= 2 and pulos[j] == 'S') or (tiros[j] > 2 and pulos[j] == 'J'):
            counter += 1
        
    print(counter)