def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('ERRO! Digite um numero válido.')
    return valor


num = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero: {num}')
