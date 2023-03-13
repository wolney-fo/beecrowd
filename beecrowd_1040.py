grades = list(map(float, input().split()))

mean = (grades[0] * 2 + grades[1] * 3 + grades[2] * 4 + grades[3]) / 10

print('Media: {:.1f}'.format(mean))

if mean < 5:
    print('Aluno reprovado.')

elif mean < 7:
    print('Aluno em exame.')

    final_test_grade = float(input())

    print('Nota do exame: {:.1f}'.format(final_test_grade))

    mean = (mean + final_test_grade) / 2

    if mean >= 5:
        print('Aluno aprovado.') 
    else:
        print('Aluno reprovado.')
    
    print('Media final: {:.1f}'.format(mean))

else:
    print('Aluno aprovado.')