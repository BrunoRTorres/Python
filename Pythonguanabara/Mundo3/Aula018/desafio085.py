valores = [[], []]

for i in range(0, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        valores[0].append(num)
    if num % 2 == 1:
        valores[1].append(num)

print(f'Os numeros pares sao: {sorted(valores[0])}')
print(f'Os numeros impares sao: {sorted(valores[1])}')
