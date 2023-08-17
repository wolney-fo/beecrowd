n = int(input())

for _ in range(n):
    p = input()

    if len(p) == 3:
        counter = 0
        x = 'one'
        for i in range(3):
            if p[i] != x[i]:
                counter += 1
        if counter <= 1:
          print(1)
        else:
          print(2)
    else:
          print(3)