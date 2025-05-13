num = int(input('Digite um numero inteiro: '))

cont = 0

for c in range(1, num + 1):

    if num % c == 0:

        cont += 1

        print('\33[33m', end=' ')
    
    else:

        print('\33[31m', end=' ')

    print('{} '.format(c), end=' ',)

print('\33[mO numero {} foi divisivel {} vezes'.format(num, cont))

if cont == 2:

    print('E por isso ele e PRIMO!')

else:

    print('E por isso ele NAO e PRIMO!')