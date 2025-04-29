r1 = float(input('primeiro lado: '))

r2 = float(input('Segundo lado: '))

r3 = float(input('Terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')

    if r1 == r2 == r3:

        print('EQUILATERO')
    
    elif r1 != r2 != r3 != r1:

        print('ESCALENO')

    else:

        print('ISOCELES')

else:

    print('Os segmentos acima NAO PODEM FORMAR triangulo')
