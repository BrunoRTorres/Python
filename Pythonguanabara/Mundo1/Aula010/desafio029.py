velocidade = int(input('Qual a velocidade do carro: '))

calculoMulta = velocidade - 80

multa = 7 * calculoMulta

if velocidade >80:

    print('Seu carro esta acima da velocidade permitida!')

    print('Voce recebeu uma multa de R${}!'.format(multa))

else:

    print('Voce esta dentro da velocidade permitida!')
