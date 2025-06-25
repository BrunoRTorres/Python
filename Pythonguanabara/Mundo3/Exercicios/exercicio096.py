def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg:.2f}m X {comp:.2f}m e de {a:.2f}m².')


print(' Controle de Terrenos')
print('-' * 22)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
