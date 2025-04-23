# soma de dois lados deve ser maior que o terceiro lado

lado1 = float(input('Digite um lado do triangulo: '))

lado2 = float(input('Digite um lado do triangulo: '))

lado3 = float(input('Digite um lado do triangulo: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

    print('Com esses lados e possivel formar um triangulo.')

else:

    print('Nao e possivel formar um triangulo.')
