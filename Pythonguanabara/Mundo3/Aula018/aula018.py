# Aula de listas parte 2

#! Fundamentos

#? Cria uma copia da lista e joga dentro de outra lista
# dados = ['Pedro', 25]
# pessoas = list()
# pessoas.append(dados[:])


# pessoas = [['Pedro', 25], ['Maria', 19], ['Joao', 32]]
# print(pessoas[0][0]) #? Mostra o nome Pedro
# print(pessoas[1][1]) #? Mostra a idade 19
# print(pessoas[2][0]) #? Mostra o nome Joao
# print(pessoas[1]) #? Mostra ['Maria', 19]

#@ Pratica

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

print(galera)

print('=' * 50)

galera2 = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(galera2)
print(galera2[0])
print(galera2[0][0])
print(galera2[2][1])

print('=' * 50)

for p in galera2:
    print(p)

print('=' * 50)

galera3 = list()
dado = list()
totmaior = totmenor = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()

for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} e menor de idade.')
        totmenor += 1

print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
print(galera3)

print('=' * 50)
