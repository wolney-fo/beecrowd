while True:
    try:
        num = float(input())
        cutoff = float(input())

        decimais = num - int(num)
        
        result = int(num) + 1 if decimais >= cutoff else int(num)
        
        print(result)

    except EOFError:
        break