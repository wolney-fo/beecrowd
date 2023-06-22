inp = [int(x) for x in input().split(" ")]
ms = inp[1]

for i in range(inp[0]):
    inp[1] += int(input())
    if inp[1] < ms:
        ms = inp[1]

print(ms)
