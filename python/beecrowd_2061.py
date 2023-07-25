inp = [int(x) for x in input().split(" ")]

for i in range(inp[1]):
    act = input()

    if act == "fechou":
        inp[0] += 1
    else:
        inp[0] -= 1

print(inp[0])
