extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

numero = int(input('Digite um numero de 0 a 20: '))

while 0 > numero or numero > 20:

    numero = int(input('Tente novamente. Digite um numero de 0 a 20: '))

print(f'Voce digitou o numero:', extenso[numero])
