tupla1 = (int(input('Digite um numero: ')),)

tupla2 = (int(input('Digite outro numero: ')),)

tupla3 = (int(input('Digite mais um numero: ')),)

tupla4 = (int(input('Digite o ultimo numero: ')),)

tupla = tupla1 + tupla2 + tupla3 + tupla4

print(f'Voce digitou os valores: {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)} vezes')
