qty = int(input())

for i in range(qty):
    inp = input()

    if inp[0] == inp[2]:
        print(int(inp[0]) * int(inp[2]))
    else:
        if inp[1].isupper():
            print(int(inp[2]) - int(inp[0]))
        else:
            print(int(inp[2]) + int(inp[0]))