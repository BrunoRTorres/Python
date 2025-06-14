jogador = dict()

jogador['nome'] = str(input('Nome do jogador: ')).title()
jogador['total'] = 0

partidas = int(input('Quantas partidas ele jogou? '))
for i in range(0, partidas):
    jogador[f'partida{i+1}'] = int(input(f'Quantos gols foram feitos na partida {i+1}? '))
    jogador['total'] = jogador['total'] + jogador[f'partida{i+1}']

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
#for k, v in jogador.items()
print(f'No total fez {jogador["total"]} gols.')

