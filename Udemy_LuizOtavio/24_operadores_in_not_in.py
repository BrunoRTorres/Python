# Operadores in e not in
# Strings sao iteraveis
#  0 1 2 3 4 
#  B r u n o
# -5-4-3-2-1

nome = 'Bruno'
# print(nome[2])
# print(nome[-3])
print('uno' in nome)
print('rres' in nome)
print(10 * '-')
print('uno' not in nome)
print('rres' not in nome)

nomeex = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nomeex:
    print(f'{encontrar} esta em {nomeex}')
else:
    print(f'{encontrar} nao esta em {nomeex}')
