num = soma = cont = 0

while True:

    num = int(input('Digite um numero: [999 encerra]'))

    if num == 999:

        break

    soma += num

    cont += 1

print(f'Voce informou {cont} numeros, e a soma entre eles e {soma}.')
