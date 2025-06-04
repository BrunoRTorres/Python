from random import randint

maior = menor = cont = 0

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for num in tupla:

    cont += 1

    print(num, end=' ')
    
    if cont == 1:

        maior = num

        menor = num

    else:

        if num > maior:

            maior = num

        if num < menor:

            menor = num

print('')

print(maior, menor)
