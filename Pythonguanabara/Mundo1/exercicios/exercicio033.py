numero1 = int(input('Digite um numero: '))

numero2 = int(input('Digite um numero: '))

numero3 = int(input('Digite um numero: '))

menor = numero1

if numero2 < numero1 and numero2 < numero3:

    menor = numero2

if numero3 < numero1 and numero3 < numero2:

    menor = numero3

print('O menor numero foi o {}'.format(menor))

maior = numero1

if numero2 > numero1 and numero2 > numero3:

    maior = numero2

if numero3 > numero1 and numero3 > numero2:

    maior = numero3

print('O maior numero foi o {}'.format(maior))
