t = int(input())

for _ in range(t):
    k = int(input())

    lang = s = input().strip()
    k -= 1

    while k > 0:
        s = input().strip()
        if s != lang:
            lang = 'ingles'
        k -= 1

    print(lang)