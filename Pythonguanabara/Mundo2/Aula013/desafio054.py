from datetime import date
 
maior = 0

menor = 0

for c in range(1, 8):

    ano = int(input('Em que ano voce nasceu? '))
    
    idade = date.today().year - ano

    if idade < 18:

        menor += 1

    else:

        maior += 1

print('Neste grupo de 7 pessoas, temos {} menores de idade, e {} maiores de idade'.format(menor, maior))
