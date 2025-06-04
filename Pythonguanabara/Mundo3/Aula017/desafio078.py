lista = []

for num in range(0, 5):

    lista.append(int(input('Digite um numero: ')))

print('=' * 52)

print(f'Voce criou uma lista contendo os seguintes valores: {lista}')

print('=' * 52)

for c, v in enumerate(lista):

    if v == max(lista):

        print(f'O maior valor foi o {v}, na posicao {c}')

        print('=' * 35)

    if v == min(lista):

        print(f'O menor valor foi o {v}, na posicao {c}')

        print('=' * 35)

print('PROGRAMA ENCERRADO')

print('=' * 18)
