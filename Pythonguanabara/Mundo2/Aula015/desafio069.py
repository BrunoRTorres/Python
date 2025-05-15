maior = idade = conthomem = contmulher = 0

sexo = ' '

fecha = ' '

while True:
    
    print('=-' * 14 + '=')
    
    idade = int(input('Quantos anos tem a pessoa? '))

    print('=-' * 14 + '=')

    sexo = str(input('Qual o sexo da pessoa? ')).upper().strip()[0]
    
    print('=-' * 14 + '=')

    fecha = str(input('Deseja continuar? [S/N] '))

    if idade >= 18:

        maior += 1

    if sexo in 'Mm':

        conthomem += 1

    if idade < 20 and sexo in 'Ff':
        contmulher += 1

    if fecha in 'Nn':

        break

print('=-' * 14 + '=')

print(f'No total, temos {maior} pessoas maiores de idade.')

print('=-' * 14 + '=')

print(f'No total, temos {conthomem} homens cadastrados.')

print('=-' * 14 + '=')

print(f'No total, temos {contmulher} mulheres com menos de 20 anos cadastradas.')

print('=-' * 14 + '=')
