counter = 0

while True:
    try:
        n = int(input())
        inp = [x for x in input().split()]
        
        if not counter == 0:
            print("")

        counter += 1

        f = m = 0

        for i in range(0, len(inp), 2):
            tamanho, gen = int(inp[i]), inp[i + 1]

            if(tamanho == n):
                if(gen == "F"):
                    f += 1
                else:
                    m += 1
        
        print("Caso {}:".format(counter))
        print("Pares Iguais: {}".format(f + m))
        print("F: {}".format(f))
        print("M: {}".format(m))

    except EOFError:
        break