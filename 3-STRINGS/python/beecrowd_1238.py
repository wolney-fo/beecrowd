n = int(input())

for _ in range(n):
    s1, s2 = map(str, input().split())

    x = min(len(s1), len(s2))

    res = ''

    for i in range(x):
        res += s1[i] + s2[i]

    if len(s1) > len(s2):
        res += s1[x:]
    elif len(s2) > len(s1):
        res += s2[x:]

    print(res)
