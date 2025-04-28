lado1 = float(input('O tamanho do primeiro lado: '))

lado2 = float(input('O tamanho do segundo lado: '))

lado3 = float(input('O tamanho do terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:

    print('Com esses lado e possivel formar um triangulo')

    if lado1 == lado2 == lado3:

        print('Esse triangulo e equilatero')
    
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:

        print('Esse triangulo e isosceles')

    else:

        print('Esse triangulo e escaleno')
        
else:

    print('Nao e possivel formar um triangulo')
