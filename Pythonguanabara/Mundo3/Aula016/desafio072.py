extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

numero = 0

numero = int(input('Digite um numero de 0 a 20: '))

while 0 > numero or numero > 20:    #! Consertar

    numero = int(input('Tente novamente. Digite um numero de 0 a 20: '))

print(f'Voce digitou o numero:', extenso[numero])
