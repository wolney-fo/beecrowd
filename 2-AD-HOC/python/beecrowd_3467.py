while True:
    try:
        inp = input().strip()
        if inp == 'xxL':
            print('Esse eh o meu lugar')
        else:
            print('Oi, Leonard')
    except EOFError:
        break