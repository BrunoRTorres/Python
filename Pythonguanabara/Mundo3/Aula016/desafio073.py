times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Ceara SC', 'Bahia', 'Fuminense', 'Corinthians', 'Atletico-MG', 'Botafogo', 'Sao Paulo', 'Mirassol', 'Vasco da Gama', 'Fortaleza', 'Internacional', 'EC Vitoria', 'Gremio', 'Juventude', 'Santos', 'Sport Recife')

print('=' * 90)

print(f'Os 5 primeiros times sao: {times[0:5]}.')

print('=' * 90)

print(f'Os 4 ultimos times sao: {times[16:]}.')

print('=' * 90)

print(f'Os times em ordem alfabetica: {sorted(times)}.')

print('=' * 90)

print(f'O Botafogo esta na , {times.index('Botafogo') + 1}ª posicao.')

print('=' * 90)
