valor = float(input('Qual o valor do produto? '))

desconto = 0.95

novoValor = valor * desconto

print('O produto que custava R${:.2f}, passara a custar R${:.2f} com o desconto'.format(valor, novoValor))
