numero = int(input('Digite um numero: '))
print('-=' * 8)

print('binario = 1')

print('octal = 2')

print('hexadecimal = 3')

print('-=' * 8)

conversao = int(input('Para qual base voce gostaria de converter? '))

if conversao == 1:

    binario = bin(numero).replace('0b', '')
    
    print(binario)

elif conversao == 2:

    octal = oct(numero).replace('0o', '')

    print(octal)

elif conversao == 3:

    hexadecimal = hex(numero).replace('0x', '')

    print(hexadecimal)
