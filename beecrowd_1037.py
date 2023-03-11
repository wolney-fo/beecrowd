user_input = float(input())

if user_input < 0 or user_input > 100:
    print('Fora de intervalo')

elif user_input >= 0 and user_input <= 25:
    print('Intervalo [0,25]') 

elif user_input <= 50:
    print('Intervalo (25,50]')

elif user_input <= 75:
    print('Intervalo (50,75]')

else:
    print('Intervalo (75,100]')