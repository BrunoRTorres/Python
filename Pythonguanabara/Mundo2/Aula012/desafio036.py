casa = float(input('Qual o valor da casa? R$'))

salario = float(input('Qual o seu salario? R$'))

anos = int(input('Em quantos anos voce vai pagar? '))

parcela = casa / (anos * 12)

if parcela <= salario * 0.3:

    print('Parabens! Seu emprestimo foi aprovado!')

    print('A parcela do seu imovel ficou em R${:.2f}'.format(parcela))

elif parcela > salario * 0.3:

    print('Que pena! seu emprestimo foi negado!')

    print('A parcela de {:.2f} ficou maior que 30% do seu salario'.format(parcela))
