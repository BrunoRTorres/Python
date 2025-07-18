

while True:
    primeiro_numero = input('Digite um numero: ')
    segundo_numero = input('Digite outro numero: ')
    operador = input('Digite o operador (+ - / *): ')
    
    if primeiro_numero.isnumeric() and segundo_numero.isnumeric()\
        and '+-/*' in operador:
        int_primeiro_numero = int(primeiro_numero)
        int_segundo_numero = int(segundo_numero)

        if operador == '+':
            soma = int_primeiro_numero + int_segundo_numero
            print(soma)

        if operador == '-':
            subtracao = int_primeiro_numero - int_segundo_numero
            print(subtracao)

        if operador == '/':
            divisao = int_primeiro_numero / int_segundo_numero
            print(divisao)

        if operador == '*':
            multiplicacao = int_primeiro_numero * int_segundo_numero
            print(multiplicacao)
            
    else:
        print('Voce digitou algo errado')

    sair = input('Quer sair? [S/N]: ').lower().startswith('s')

    if sair is True:
        break