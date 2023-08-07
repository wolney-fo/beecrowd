while True:
    n = int(input())

    if n == 0:
        break

    count_a = count_b = 0

    for i in range(n):
        a, b = map(int, input().split())

        if a > b:
            count_a += 1
        elif b > a:
            count_b += 1
            
    print(count_a, count_b)
