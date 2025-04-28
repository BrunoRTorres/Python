valor = float(input('Qual o valor do produto? '))

print('=-' * 5)

print('Dinheiro\nCheque\ncartao')

print('=-' * 5)

pagamento = str(input('Qual a forma de pagamento? ')).lower()

if pagamento in 'dinheiro cheque':

    novoValor = valor * .9
    print('O valor a ser pago sera R${:.2f}'.format(novoValor))

elif pagamento == 'cartao':

    print('=-' * 5)

    parcela = int(input('Em quantas parcelas? '))

    print('=-' * 5)
    
    if parcela == 1:

        novoValor = valor * .95

        print('O valor a ser pago sera R${:.2f}'.format(novoValor))
    
    elif parcela == 2:

        print('O valor a ser pago sera de R${} em 2x'.format(valor / 2))

    elif parcela <= 3:

        novoValor = valor * 1.2
        print('O valor a ser pago sera de R${:.2f} em {}x'.format(novoValor / parcela, parcela))
