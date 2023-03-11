cardapio = {
    1 : 4.0,
    2 : 4.5,
    3 : 5.0,
    4 : 2.0,
    5 : 1.5
}

user_input = list(map(int, input().split()))

print('Total: R$ {:.2f}'.format((cardapio[user_input[0]] * user_input[1])))