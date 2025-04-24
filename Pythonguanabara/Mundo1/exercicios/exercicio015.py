dia = int(input('Quantos dias alugados? '))

km = float(input('Quantos Km rodados? '))

valorDia = dia * 60

valorKm = km * .15

print('Total do aluguel: R${:.2f}'.format(valorDia + valorKm))
