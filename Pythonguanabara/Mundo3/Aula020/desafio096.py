def calcArea(largura, comprimento):
    area = largura * comprimento
    print(f'A area de um terreno {largura:.2f}m x {comprimento:.2f}m e igual a {area:.2f}m².')


largura = float(input('Largura do terreno: '))
comprimento = float(input('Comprimento do terreno: '))

calcArea(largura, comprimento)
