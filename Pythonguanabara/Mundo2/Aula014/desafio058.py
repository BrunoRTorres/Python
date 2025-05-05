from random import randint

computador = randint(0, 10)

jogador = int(input('Escolha um numero de 0 a 10: '))

tentativa = 1

while jogador != computador:

    tentativa += 1
    
    if jogador < computador:

        print('O numero que escolhi e maior!')

    if jogador > computador:

        print('O numero que escolhi e menor!')
    
    jogador = int(input('Tente novamente: '))


print('Voce acertou em {} tentativa(s)!'.format(tentativa))
