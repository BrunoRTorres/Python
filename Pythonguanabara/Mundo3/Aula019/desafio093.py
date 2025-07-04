jogador = dict()
gols = list()

print('=-' * 12 + '=')

jogador['nome'] = str(input('Nome do jogador: ')).title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}? ')))
jogador['gols'] = gols[:]

total = 0
for g in gols:
    total += g
jogador['total'] = total

print('=-' * 16 + '=')

print(f'O jogador {jogador["nome"]} jogou {len(gols)} partidas.')
for p, g in enumerate(jogador['gols']):
    print(f'Na partida {p+1} fez {g} gols.')

print(f'O jogador {jogador["nome"]} marcou um total de {jogador["total"]} gols.')

print('=-' * 21 + '=')