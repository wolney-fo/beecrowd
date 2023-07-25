evenValues = oddValues = positiveValues = negativeValues = 0

for i in range(5):
    inputValue = int(input())

    if inputValue > 0:
        positiveValues += 1

    elif inputValue < 0:
        negativeValues += 1

    if inputValue % 2 == 0:
        evenValues += 1
    
    else:
        oddValues += 1

print('{} valor(es) par(es)'.format(evenValues))
print('{} valor(es) impar(es)'.format(oddValues))
print('{} valor(es) positivo(s)'.format(positiveValues))
print('{} valor(es) negativo(s)'.format(negativeValues))