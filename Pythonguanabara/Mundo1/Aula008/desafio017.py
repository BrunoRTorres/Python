import math
catetoA = int(input('Digite o lado do cateto adjacente: '))

catetoO = int(input('Digite o lado do cateto oposto: '))

hipotenusa = catetoA ** 2 + catetoO ** 2

print('A hipotenusa do triangulo com os lados {} e {} e igual a {}'.format(catetoA, catetoO, math.sqrt(hipotenusa)))
