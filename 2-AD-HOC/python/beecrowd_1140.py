while True:
    inp = [x for x in input().split()]
    if (len(inp) == 1 and inp[0] == '*'):
        break

    out = 'Y'

    for w in inp:
        if w[0].upper() != inp[0][0].upper():
            out = 'N'
            break
    print(out)