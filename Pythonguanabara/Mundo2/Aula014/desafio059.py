valor1 = int(input('Digite o primeiro valor: '))

valor2 = int(input('Digite o segundo valor: '))


escolha = 0

while escolha != 5:

    print('=-' * 12 + '=')

    print('''
          [1] somar
          [2] multiplicar
          [3] maior
          [4] novos numeros
          [5] sair
          ''')
    
    print('=-' * 12 + '=')

    escolha = int(input('O que deseja fazer? '))

    if escolha == 1:

        soma = valor1 + valor2

        print('=-' * 12 + '=')

        print('A soma entre {} e {} = {}'.format(valor1, valor2, soma))

    if escolha == 2:

        multi = valor1 * valor2

        print('=-' * 12 + '=')

        print('A multiplicacao entre {} e {} = {}'.format(valor1, valor2, multi))

    if escolha == 3:

        if valor1 < valor2:
            
            print('=-' * 12 + '=')

            print('{} e maior que {}'.format(valor2, valor1))

        elif valor1 > valor2:

            print('=-' * 12 + '=')
            
            print('{} e maior que {}'.format(valor1, valor2))
    
    if escolha == 4:

        print('=-' * 12 + '=')
        
        valor1 = int(input('Digite o primeiro valor: '))

        valor2 = int(input('Digite o segundo valor: '))

print('=-' * 8 + '=')

print('Tenha um bom dia!')

print('=-' * 8 + '=')
