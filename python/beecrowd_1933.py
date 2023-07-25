cards = list(map(int, input().split()))

if (cards[0] == cards[1]):
    print(cards[0])

else:
    if cards[0] > cards[1]:
        print(cards[0])
    else:
        print(cards[1])