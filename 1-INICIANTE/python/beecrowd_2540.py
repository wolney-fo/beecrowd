while True:
    try:
        qty = int(input())

        inp = [int(x) for x in input().split()]

        if inp.count(1) >= qty * (2/3):
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError:
        break
