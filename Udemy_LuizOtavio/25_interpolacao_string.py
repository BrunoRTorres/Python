'''
Interpolacao basica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''

nome = 'Bruno'
preco = 1000.9589743
variavel = '%s, o preco e R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d e %08X' % (1500, 1500))
