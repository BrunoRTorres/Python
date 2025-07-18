"""
    ? break - Interrompe o while mais proximo,
    ? e retorna para a linha de codigo

    ? continue - Encerra o loop, e retorna para o inicio
    ? do while mais proximo
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('O  valor 6 foi pulado')
        continue
    
    if contador > 10 and contador <= 27:
        print('Nao vou mostrar o', contador)
        continue
    
    print(contador)

    if contador == 40:
        break

print('Acabou')
