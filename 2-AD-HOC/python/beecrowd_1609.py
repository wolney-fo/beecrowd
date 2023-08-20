t = int(input())

for _ in range(t):
    counter = 1

    n = int(input())

    inp = [int(x) for x in input().split()]
    inp.sort()

    for i in range(1, n):
        if inp[i] != inp[i - 1]:
            counter += 1

    print(counter)