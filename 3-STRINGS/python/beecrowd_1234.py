while True:
    try:
        inp = input()
        up = True
        for l in inp:
            if (up):
                print(l.upper(), end='')
            else:
                print(l.lower(), end='')
            if l != ' ':
                up = not up
        print()

    except EOFError:
        break