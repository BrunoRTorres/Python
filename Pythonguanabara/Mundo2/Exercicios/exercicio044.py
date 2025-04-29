print('{:=^40}'.format(' LOJAS TORRES '))

preco = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
      [ 1 ] a vista dinheiro/cheque
      [ 2 ] a vista cartao
      [ 3 ] 2x no cartao
      [ 4 ] 3x ou mais no cartao''')

opcao = int(input('Qual e a opcao? '))

if opcao == 1:

    total = preco * 0.9

elif opcao == 2:

    total = preco * 0.95

elif opcao == 3:
    
    total = preco

    parcela = total / 2

    print('Sua compra sera parcelada em 2x de R${:.2f}'.format(parcela))

elif opcao == 4:

    total = preco * 1.2

    totparc = int(input('Quantas parcelas? '))

    parcela = total / totparc

    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))

else:

    total = preco

    print('OPCAO INVALIDA de pagamento. Tente novamente')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
