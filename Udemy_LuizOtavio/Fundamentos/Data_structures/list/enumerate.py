"""
    ! Enumerate - enumera iteraveis (indices)
"""

lista = ['Pamela', 'Alice', 'Bruno']
lista.append('Outro valor')

# lista_enumerate = enumerate(lista)

# for item in lista_enumerate:
#     print(item)

for indice, nome in enumerate(lista):
    print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')