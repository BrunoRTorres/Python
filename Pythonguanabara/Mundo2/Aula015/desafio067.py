num = 0

while True:

    valor = int(input('Digite um numero para ver a tabuada: '))

    if valor < 0:

        break

    for num in range(1, 11):

        produto = valor * num

        print(f'{valor} X {num:2} = {produto}')
