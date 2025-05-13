from random import randint, choice

soma = cont = 0

parimpar = ''

computador = randint(1, 5)

computadorparimpar = choice(['P', 'I'])

while True:

    jogador = int(input('Jogue um numero de 1 a 5: '))

    parimpar = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]

    
