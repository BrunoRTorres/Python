lista = []

while True:

    lista.append(int(input('Digite um numero: ')))

    saida = ' '

    while saida not in 'sn':

        saida = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

    if saida == 'n':

        break

print('=' * 36)

print(f'Voce criou a lista: {lista}')

listaImpar = lista[:]

listaPar = lista[:]

for num in lista:

    if num % 2 == 0:

        listaImpar.remove(num)

    else:

        listaPar.remove(num)

print('=' * 36)

print(f'Os numeros impares da lista: {listaImpar}')

print('=' * 36)

print(f'Os numeros pares da lista: {listaPar}')

print('=' * 36)
