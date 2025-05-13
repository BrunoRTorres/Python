'''
faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo
'''

num = int(input('Digite um numero inteiro: '))

cont = 0

for i in range(1, num +1):

    if num % i == 0:

        cont += 1

if cont == 2:

    print('O numero {} foi dividido {} vezes, por isso ele e primo'.format(num, cont))

else:

    print('O numero {} foi dividido {} vezes, por isso ele nao e primo'.format(num, cont))
