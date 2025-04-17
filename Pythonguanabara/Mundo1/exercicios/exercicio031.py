distancia = float(input('Qual e a distancia da sua viagem? '))

print('Voce esta prestes a comecar uma viagem de {:.2f}Km')

if distancia <= 200:

    preco = distancia * 0.5

else:

    preco = distancia * 0.45

print('O preco da sua passagem sera de R${:.2f}'.format(preco))
