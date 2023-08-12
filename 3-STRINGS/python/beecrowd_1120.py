while True:
    d, n = map(str, input().split())

    if d == n == '0':
        break

    n = n.replace(d, '')
    n = n.lstrip('0')

    if n == '':
        n = '0'

    print(n)