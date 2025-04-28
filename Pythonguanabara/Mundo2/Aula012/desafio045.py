from random import choice

print('=-' * 5)

print('Pedra\nPapel\nTesoura')

print('=-' * 5)

jogador = str(input('Qual voce ira jogar? ')).lower()

lista = ['Pedra', 'Papel', 'Tesoura']

computador = choice(lista)

if jogador == 'pedra':

    if computador == 'Pedra':

        print('=-' * 5)

        print('Deu empate!')
    
    elif computador == 'Papel':

        print('=-' * 5)

        print('Voce perdeu!')
    
    elif computador == 'Tesoura':

        print('=-' * 5)

        print('Voce ganhou!')
    
if jogador == 'papel':
    
    if computador == 'Pedra':

        print('=-' * 5)

        print('Voce ganhou!')
    
    elif computador == 'Papel':

        print('=-' * 5)

        print('Deu empate!')

    elif computador == 'Tesoura':

        print('=-' * 5)

        print('Voce perdeu!')

if jogador == 'tesoura':

    if computador == 'Pedra':

        print('=-' * 5)

        print('Voce perdeu!')

    elif computador == 'Papel':

        print('=-' * 5)

        print('Voce ganhou')

    elif computador == 'Tesoura':

        print('=-' * 5)

        print('Deu empate!')

else:

    print('=-' * 5)

    print('Comando invalido!')
