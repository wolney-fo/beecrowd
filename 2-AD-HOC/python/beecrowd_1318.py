while True:
    n, m = map(int, input().split())

    if (n == m == 0):
        break

    inp = [int(x) for x in input().split()]

    inp.sort()

    counter = 0
    index = 1

    while (index <= len(inp) - 1):
        if (inp[index - 1] == inp[index]):
            num = inp[index]
            
            while (inp[index] == num):
                if (index == len(inp) - 1):
                    break
                index += 1
            
            counter += 1
        index += 1

    print(counter)
