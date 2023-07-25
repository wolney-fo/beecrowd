pri = {
        1001: 1.5,
        1002: 2.5,
        1003: 3.5,
        1004: 4.5,
        1005: 5.5
}

x = 0

for i in range(int(input())):
    inp = [int(x) for x in input().split(" ")]
    x += pri[inp[0]] * inp[1]

print("{:.2f}".format(x))
