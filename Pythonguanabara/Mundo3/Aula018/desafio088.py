from random import sample
from time import sleep

jogos = []
numeros = list(range(1, 61))
temp = []

print('=' * 32)

quantJogos = int(input('Quantos jogos gostaria de ver? '))

for i in range(0, quantJogos):
    temp = sample(numeros, 6)
    jogos.append(temp[:])
    temp.clear()

print('=' * 32)

for i, j in enumerate(jogos):
    print(f'{i + 1}o jogo: {sorted(j)}')
    sleep(.5)

print('=' * 32)
