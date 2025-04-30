# Aula de repeticoes controladas

#! Estrutura 

#? for c in range(0, 4):

#?    print(c)

#? print('Acabou')

#@ pratica

print('=-' * 10 + '=')

for c in range(1, 6):

    print('Oi')

print('=-' * 10 + '=')


for c in range(7, 0, -1):

    print(c)

print('=-' * 10 + '=')


for c in range(1, 7, 2):

    print(c)

print('=-' * 10 + '=')


n = int(input('Digite um numero: '))

for c in range(0, n+1):

    print(c)

print('=-' * 10 + '=')


i = int(input('Inicio: '))

f = int(input('Fim: '))

p = int(input('Passo: '))

for c in range(i, f+1, p):

    print(c)

print('=-' * 10 + '=')


s = 0

for c in range(0, 4):

    n = int(input('Digite um valor: '))

    s += n

print('O somatorio de todos os valores foi {}'.format(s))

print('=-' * 10 + '=')
