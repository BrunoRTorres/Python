jogador = dict()
gols = list()
time = list()

print('=-' * 12 + '=')

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    print('=-' * 30 + '=')

    while True:
        continuar = str(input('Deseja adicionar mais um jogador? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Use somente S ou N.')
    
    if continuar == 'N':
        break
print('=-' * 30 + '=')

print()
for k, v in enumerate(time):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()