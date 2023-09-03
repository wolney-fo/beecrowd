inp = input()

if not (inp.count('X') == 2 and inp.count('O') == 1):
    print('?')
elif inp[1] == 'O':
    print('*')
else:
    print('Alice')