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

print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<13}', end='')
print()

for k, v in enumerate(time):
    print(f'{k:>2}  ', end='')
    for d in v.values():
        print(f'{str(d):<13}', end='')
    print()

while True:
    escolha = int(input('Deseja ver os dados de qual jogador? '))
    if escolha == 999:
        print('Encerrando...')
        break
    print('=-' * 20 + '=')
    if escolha >= len(time):
        print(f'ERRO! jogador com Cod {escolha} nao existe!')
    else:
        print(f'Historico do jogador {time[escolha]["nome"]}')
        for i, g in enumerate(time[escolha]["gols"]):
            print(f'    Na partida {i+1} marcou {g} gols.')
        print('=-' * 20 + '=')