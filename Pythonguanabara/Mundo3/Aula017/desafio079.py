lista = []

while True:
        
    num = int(input('Digite um numero: '))

    if num not in lista:

        lista.append(num)

        print('Numero adicionado com sucesso')

    else:

        print('Numero existente... Tente novamente')

    saida = ' '

    while saida not in 'sn':

        saida = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

    if saida == 'n':

        break

lista.sort()

print('=' * 30)

print(lista)
