num = int(input('Digite um numero inteiro: '))

for c in range(1, num + 1):

    if num % c == 0:

        print('\33[33m', end=' ')
    
    else:

        print('\33[31m', end=' ')

    print('{} '.format(c), end=' ',)
