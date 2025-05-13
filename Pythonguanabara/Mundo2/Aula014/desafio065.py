num = cont = media = maior = total =  0

sair = ''

while sair != 'N':

    num = int(input('Digite um numero: '))

    sair = str(input('Deseja continuar? [S/N] ')).upper().strip()

    total += num

    cont += 1

    media = total / cont

    if cont == 1:

        maior = menor = num

    else:

        if num > maior:

            maior = num

        else:

            menor = num

print('Voce digitou {} numeros, a media entre eles foi {}'.format(cont, media))

print('O maior foi {} e o menor foi {}'.format(maior, menor))
