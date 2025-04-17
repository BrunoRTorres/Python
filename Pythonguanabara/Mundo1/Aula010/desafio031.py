distancia = float(input('Qual a distancia da viagem em Km: '))

if distancia <=200:

    print('O valor desta viagem sera R${:.2f}'.format(distancia * 0.5))

else:

    print('O valor desta viagem sera R${:.2f}'.format(distancia * 0.45))
