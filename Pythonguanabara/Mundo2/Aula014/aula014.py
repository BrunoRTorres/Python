# Aula de repeticoes com teste logico

#! Estrutura

#? while not teste:

#?    if teste:

#?        print()

#?    if teste:

#?        print()

#? print()

#@ Pratica

'''for c in range(1, 11):
        
        print(c)
'''

c = 1

while c < 11:

    print(c)

    c += 1

print('=-' * 8 + '=')



n = 1

while n != 0:

    n = int(input('Digite um valor: '))

print('=-' * 8 + '=')



r = 'S'

while r == 'S':

    n = int(input('Digite um valor: '))

    r = str(input('Quer continuar? [S/N] ')).upper()

print('=-' * 8 + '=')



n = 1

par = impar = 0

while n != 0:

    n = int(input('Digite um numero? '))

    if n != 0:

        if n % 2 == 0:

            par += 1

        if n % 2 == 1:

            impar += 1

print('Voce digitou {} numero pares e {} numeros impares!'.format(par, impar))

print('=-' * 8 + '=')
