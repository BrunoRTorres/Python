lista = []

cont = 0

while True:

    lista.append(int(input('Digite um numero: ')))

    cont += 1

    saida = ' '

    while saida not in 'sn':

        saida = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

    if saida == 'n':

        break

print('=' * 30)

print(f'Foram digitados {cont} numeros.')

lista.sort(reverse=True)

print(f'A lista em ordem decrescente: {lista}')

if 5 in lista:

    print('O numero 5 se encontra na lista!')

else:

    print('O numero 5 nao foi localizado na lista!')
