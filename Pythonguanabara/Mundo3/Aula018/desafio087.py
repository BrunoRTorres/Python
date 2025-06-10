matriz = []
par = terceira = maiorSegunda = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite um valor para [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            par += matriz[i][j]
    print()
print(f'A soma dos valores par: {par}')

for i in range(0, 3):
    terceira += matriz[i][2]
print(f'A soma da terceira coluna: {terceira}')

for j in range(0, 3):
    if j == 0:
        maiorSegunda = matriz[1][j]
    elif matriz[1][j] > maiorSegunda:
        maiorSegunda = matriz[1][j]
print(f'O maior valor da segunda coluna: {maiorSegunda}')
