import random

numero = random.randrange(0, 5)

numeroEscolha = int(input('Escolha um numero entre 0 e 5: '))

if numeroEscolha == numero:

    print('Parabens, voce ganhou!')

else:

    print('Que pena, voce perdeu!')
    print('O numero certo era o {}'.format(numero))
