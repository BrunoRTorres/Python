# Aula de Tuplas

#! Fundamentos

'''

Tuplas sao imutaveis


'''
#@ Pratica

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(lanche)

print(lanche[1])

print(lanche[3])

print(lanche[-1])

print(lanche[1:3])

print(lanche[2:])

print(lanche[:2])

print('=' * 25)

for comida in lanche:

    print(f'Eu vou comer {comida}')

print('=' * 25)

for pos, comida in enumerate(lanche):       #? Duas maneiras com o mesmo resultado

    print(f'Eu vou comer {comida} na posicao {pos}')

print('=' * 25)

for cont in range(0, len(lanche)):

    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')

print(sorted(lanche)) #? ordena a tupla, mas nao altera

a = (2, 5, 4)

b = (5, 8, 1, 2)

print(a)

print(b)

c = a + b

print(c)

print(len(c))

print(c.count(5))

print(c.index(8))

print(c.index(2, 1))

pessoa = ('Gustavo', 39, 'M', 99.88)

del(pessoa) #? As tuplas so podem ser modificadas se deletadas interamente, nao podendo apagar um item somente

print(pessoa)
