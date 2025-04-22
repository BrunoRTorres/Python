salario = float(input('Digite o salario do funcionario: R$'))

if salario > 1250:

    print('O seu novo salario com 10% de aumento sera R${:.2f}'.format(salario * 1.1))

else:

    print('O seu novo salario com 15% de aumento sera R${:.2f}'.format(salario * 1.15))
