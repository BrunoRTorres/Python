while True:

    n = int(input('Quer ver a tabuada de qual valor? '))

    print('-' * 30)

    if n < 0:

        break

    for c in range(1, 11):

        print(f'{n} X {c:2} = {n * c}')
    
    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
