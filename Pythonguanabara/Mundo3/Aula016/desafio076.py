lista = ('lapis', 5, 'Borracha', 2, 'Caneta', 6, 'Caderno', 15, 'Mochila', 100, 'Estojo', 7)

for pos in range(0, len(lista)):

    if pos % 2 == 0:

        print(f'{lista[pos]:.<30}', end='')

    else:

        print(f'R${lista[pos]:>7.2f}')