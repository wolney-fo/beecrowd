alcool = 0      # 1
gasolina = 0    # 2
diesel = 0      # 3

while True:

    clientAnswer = 0

    while clientAnswer < 1 or clientAnswer > 4: # get the right code
        clientAnswer = int(input())

    if clientAnswer == 1:
        alcool += 1

    elif clientAnswer == 2:
        gasolina += 1

    elif clientAnswer == 3:
        diesel += 1
        
    else:
        break


print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))