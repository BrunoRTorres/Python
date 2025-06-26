from time import sleep

def maior(*  num):
    cont = maior = 0
    
    print('-=' * 30)
    print('Analisando os valores passados...')

    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')



maior(1, 2, 3)
maior(4, 6, 7, 3)
maior()
maior(1)
maior(5, 2, 1, 6, 8, 9, 0, 77, 42, 56, 1921)
