tupla1 = (int(input('Digite um numero: ')),)

tupla2 = (int(input('Digite outro numero: ')),)

tupla3 = (int(input('Digite mais um numero: ')),)

tupla4 = (int(input('Digite o ultimo numero: ')),)

tupla = tupla1 + tupla2 + tupla3 + tupla4

print(f'Voce digitou os valores: {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:

    print(f'O numero 3 apareceu na {tupla.index(3) + 1}ª posicao')

else:

    print('O numero 3 nao apareceu na tupla')

print('Os numeros pares da tupla:', end=' ')

for n in tupla:

    if n % 2 == 0:

        print(n, end=' ')
