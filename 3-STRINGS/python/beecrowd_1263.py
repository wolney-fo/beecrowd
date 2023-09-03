while True:
    try:
        letras = [x[0].upper() for x in input().split()]
        counter = 0
        index = 1

        while index < len(letras):
            if letras[index] == letras[index-1]:
                while index < len(letras) and letras[index] == letras[index-1]:
                    index += 1
                counter += 1
            else:
                index += 1

        print(counter)

    except EOFError:
        break