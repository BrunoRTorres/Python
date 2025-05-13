from random import randint

soma = cont = 0

parimpar = ' '

while True:

    print('=-' * 10 + '=')

    jogador = int(input('Jogue um numero de 1 a 5: '))

    print('=-' * 10 + '=')

    parimpar = str(input('Par ou Impar? [P/I] ')).upper().strip()

    computador = randint(0, 5)

    soma = jogador + computador

    print('=-' * 10 + '=')

    print(f'Voce escolheu {jogador} e o computador {computador} e deu {soma}')

    print('=-' * 10 + '=')

    if soma % 2 == 0:
        
        print('Deu par!', end=' ')

    else:

        print('Deu impar!', end=' ')

    if parimpar == 'P' and soma % 2 == 0:

        print('\033[32mVoce ganhou!\033[m')

        cont += 1

    else: 

        print('\033[31mVoce perdeu!\033[m')
        
        break

print('=-' * 10 + '=')

print(f'Voce venceu {cont} partida(s) seguida(s)!')

print('=-' * 10 + '=')
