carteira = float(input('Quantos reais voce tem na carteira? R$'))

dollar = 5.78

euro = 6.35

conversorDollar = carteira / dollar

conversorEuro = carteira / euro

print('Com R${:.2f} voce pode comprar US${:.2f} ou €{:.2f}'.format(carteira, conversorDollar, conversorEuro))
