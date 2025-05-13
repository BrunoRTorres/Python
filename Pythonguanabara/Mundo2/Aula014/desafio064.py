num = 0

cont = 0

total = 0

while num != 999:

    num = int(input('Digite um numero [999 encerra]: '))

    total += num

    cont += 1

print('Voce informou {} numeros, e a soma entre eles e {}'.format(cont - 1, total - 999))
