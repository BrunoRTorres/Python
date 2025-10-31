# import os
# lista_compras = []

# while True:
#     print('Selecione uma opcao')
#     entrada = input('[i]nserir [a]pagar [l]istar: ')

#     if 'i' in entrada:
#         os.system('cls')
#         inserir = input('Valor a ser inserido: ')
#         lista_compras.append(inserir)
    
#     if 'l' in entrada:
#         if len(lista_compras) >= 1:
#             os.system('cls')
#             for indice, item in enumerate(lista_compras):
#                 print(indice, item)
#         else:
#             print('Nada a ser listado.')

#     if 'a' in entrada:
#         if len(lista_compras) >= 1:
#             os.system('cls')
#             indice = input('Valor a ser apagado: ')
#             indice = int(indice)
#             lista_compras.pop(indice)
#         else:
#             print('Nao existe valores a apagar.')


#! Resolução do professor
import os

lista = []
while True:
    print('Selecione uma opcao')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite um numero int.')
        except IndexError:
            print('Indice nao existe na lista.')
        except Exception:
            print('Erro desconhecido.')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar.')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')