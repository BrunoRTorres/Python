casa = float(input('Valor da casa: R$'))

salario = float(input('Salario do comprador: R$'))

anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)

minimo = salario * 0.3

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')

print(' a prestacao sera de R${:.2f}'.format(prestacao))

if prestacao <= minimo:

    print('Emprestimo pode ser CONCEDIDO!')

else:
    
    print('Emprestimo NEGADO!')
