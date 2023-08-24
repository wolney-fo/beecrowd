n = int(input())

for _ in range(n):
    word = input()
    mid = len(word) // 2
    l = word[:mid]
    r = word[mid:]

    l = l[::-1]
    r = r[::-1]

    print(l + r)