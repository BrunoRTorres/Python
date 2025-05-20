time = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Ceara SC', 'Bahia', 'Fuminense', 'Corinthians', 'Atletico-MG', 'Botafogo', 'Sao Paulo', 'Mirassol', 'Vasco da Gama', 'Fortaleza', 'Internacional', 'EC Vitoria', 'Gremio', 'Juventude', 'Santos', 'Sport Recife')

print('=' * 90)

print(f'Os 5 primeiros times sao: {time[0:5]}.')

print('=' * 90)

print(f'Os 4 ultimos times sao: {time[16:]}.')

print('=' * 90)

print(f'Os times em ordem alfabetica: {sorted(time)}.')

print('=' * 90)

print(f'O Botafogo esta na , {time.index('Botafogo') + 1}ª posicao.')

print('=' * 90)
