'''
faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
e menor peso lidos
'''
maior = 0

menor = 0

for pess in range(1, 6):

    peso = float(input('Qual o peso da {}ª pessoa? '.format(pess)))

    if pess == 1:

        maior = peso

        menor = peso

    else:

        if peso > maior:

            maior = peso

        if peso < menor:

            menor = peso

print('Peso maior: {:.2f}Kg'.format(maior))

print('Peso menor: {:.2f}Kg'.format(menor))
