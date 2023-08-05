while True:
    try:
        botas = {}
        counter = 0

        n = int(input())

        for i in range(n):
            num, pe = input().split()
            num = int(num)

            if num in botas:
                if pe == 'E':
                    botas[num][0] += 1
                else:
                    botas[num][1] += 1
            else:
                if pe == 'E':
                    botas[num] = [1, 0]
                else:
                    botas[num] = [0, 1]

        counter = sum(min(valores) for valores in botas.values())

        print(counter)

    except EOFError:
        break
