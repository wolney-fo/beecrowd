while True:
    n = int(input())

    if n == 0:
        break

    li = {key: True for key in range(1, n+1)}

    for i in range(2, n+1):
        for j in range(i, n+1, i):
            li[j] = not li[j]

    liPri = []
    
    for key, value in li.items():
        if value is True:
            liPri.append(key)

    print(*liPri)

