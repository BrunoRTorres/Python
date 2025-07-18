

# while True:
#     primeiro_numero = input('Digite um numero: ')
#     segundo_numero = input('Digite outro numero: ')
#     operador = input('Digite o operador (+ - / *): ')
    
#     if operador not in '+-/*':
#         print('Operador invalido.')
#         continue

#     if len(operador) > 1:
#         print('Digite apenas um operador.')
#         continue

#     if primeiro_numero.isnumeric() and segundo_numero.isnumeric():
#         int_primeiro_numero = int(primeiro_numero)
#         int_segundo_numero = int(segundo_numero)

#         if operador == '+':
#             soma = int_primeiro_numero + int_segundo_numero
#             print(soma)
#         elif operador == '-':
#             subtracao = int_primeiro_numero - int_segundo_numero
#             print(subtracao)
#         elif operador == '/':
#             divisao = int_primeiro_numero / int_segundo_numero
#             print(divisao)
#         elif operador == '*':
#             multiplicacao = int_primeiro_numero * int_segundo_numero
#             print(multiplicacao)
            
#     else:
#         print('Voce digitou um numero invalido')
#         continue

#     sair = input('Quer sair? [S/N]: ').lower().startswith('s')

#     if sair is True:
#         break


#! Solucao do professor

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os numeros digitados sao invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo.')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
