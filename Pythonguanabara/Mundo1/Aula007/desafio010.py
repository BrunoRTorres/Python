carteira = float(input('Digite o saldo da carteira: '))

cotacao = 5.78

conversor = carteira / cotacao

print('Slado na carteira: {} \ncotacao dollar: {} \nvalor disponivel para compra: {:.2f}'.format(carteira, cotacao, conversor))
