testes = int(input())
total = 0
for i in range(testes):
    data = [int(x) for x in input().split(" ")]
    total += data[0] * data[1]
print(total)
