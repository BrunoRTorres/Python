from time import sleep

n1 = int(input('Primeiro valor: '))

n2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:

    print('''
          [1] somar
          [2] multiplicar
          [3] maior
          [4] novos numeros
          [5] sair do programa
          ''')
    
    opcao = int(input('>>>>> Qual e a sua opcao? '))

    if opcao == 1:

        soma = n1 + n2

        print('A soma entre {} e {} e {}'.format(n1, n2, soma))

    elif opcao == 2:

        produto = n1 * n2

        print('O resultado de {} e {} e {}'.format(n1, n2, produto))

    elif opcao == 3:

        if n1 > n2:

            maior = n1
        
        else:

            maior = n2

        print('Entre {} e {} o maior valor e {}'.format(n1, n2, maior))

    elif opcao == 4:

        print('Informe os numeros novamente:')

        n1 = int(input('Primeiro valor: '))

        n2 = int(input('Segundo valor: '))

    elif opcao == 5:

        print('Finalizando...')

    else:

        print('Opcao invalida. Tente novamente')

    print('=-=' * 10)

    sleep(1.5)
print('Fim do programa! Volte sempre!')