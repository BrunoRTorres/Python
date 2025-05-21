times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Ceara SC', 'Bahia', 'Fuminense', 'Corinthians', 
        'Atletico-MG', 'Botafogo', 'Sao Paulo', 'Mirassol', 'Vasco da Gama', 'Fortaleza', 'Internacional', 
        'EC Vitoria', 'Gremio', 'Juventude', 'Santos', 'Sport Recife', 'teste')

print('-=' * 15)

print(f'Lista de times do Brasileirao: {times}')

print('-=' * 15)

print(f'Os 5 primeiros sao: {times[0:5]}')

print('-=' * 15)

print(f'Os 4 ultimos sao: {times[-4:]}')

print('-=' * 15)

print(f'O Botafogo esta na {times.index('Botafogo') + 1}ª posicao')
