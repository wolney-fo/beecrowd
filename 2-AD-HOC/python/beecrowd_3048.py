seq = []
x = 1

for i in range(int(input())):
    num = int(input())
    seq.append(num)
    if num != seq[i-1]:
        x += 1
print(x)
