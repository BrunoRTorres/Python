from math import hypot

catetoO = float(input('O comprimento do cateto oposto: '))

catetoA = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(catetoA, catetoO)

print('A hipotenusa vai medir {}'.format(hipotenusa))
