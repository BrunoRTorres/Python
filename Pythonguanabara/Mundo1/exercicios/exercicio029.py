velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade > 80:

    print('Multado! Voce excedeu o limite permitido que e de 80Km/H h')

    multa = (velocidade - 80) * 7

    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa)) 

print('Tenha um bom dia! Dirija com seguranca!')
