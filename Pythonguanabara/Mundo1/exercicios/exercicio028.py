from random import randint
from time import sleep

computador = randint(0, 5) # faz o computador escolher entre 0 e 5

print('-=-' * 20)

print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')

print('-=-' * 20)

jogador = int(input('Em que numero eu pensei? ')) # jogador escolhe entre 0 e 5

print('Processando...')

sleep(1)

if jogador == computador:

    print('Parabens! Voce conseguiu me vencer!')

else:

    print('Ganhei! Eu pensei no numero {} e nao no {}!'.format(computador, jogador))
