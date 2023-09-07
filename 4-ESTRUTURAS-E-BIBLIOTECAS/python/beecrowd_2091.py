while True:
    n = int(input())

    if n == 0:
        break

    inp = [int(x) for x in input().split()]

    solitario = 0

    for num in inp:
        solitario ^= num

    print(solitario)
