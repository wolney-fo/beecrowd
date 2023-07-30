while True:
    q = int(input())

    if q == 0:
        break

    inp = [int(x) for x in input().split()]

    m = inp.count(0)
    j = q-m

    print('Mary won {} times and John won {} times'.format(m, j))