valor = int(input('Digite um numero inteiro: '))

num = 0

num1= 0

num2 = 1

i = 0

while i < valor:

    print(num1, end=' ')

    num = num1 + num2

    num2 = num1

    num1 = num

    i += 1

