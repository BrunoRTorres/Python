# Aula de listas

#! Fundamentos

'''
teste = ['teste', 'teste']

#? listas sao mutaveis

teste[1] = 'revisado' 

teste.append('aprovado') #? pode ser adicionado itens

teste.insert(0, 'criacao') #? abre espaco na lista realocando os itens e adicionando o item no espaco desejado

del teste[2]

teste.pop(2) #? normalmente usado para remover o ultimo item, mas pode remover o espaco desejado

teste.remove('revisado') #? remove o item desejado usando o valor dele

#? e possivel criar listas usando o range

valores = list(range(4, 11))

valores = [8, 2, 5, 4, 9, 3, 0]

valores.sort() #? arruma os valores em ordem crescente

valores.sort(reverse=True) #? arruma os valores em ordem decrescente

len(valores) #? mostra o comprimento da lista / valores = 7

'''

#@ Pratica

num = [2, 2, 3, 9]

num[2] = 9

print(num)

num.append(7)

print(num)

num.sort()

print(num)

num.sort(reverse=True)

print(num)

num.insert(2, 0)

print(num)

if 5 in num:

    num.remove(5)

else:

    print('Nao achei o valor 5')

print(num)

valores = []

print('=' * 30)

valores.append(5)

valores.append(9)

valores.append(4)

print(valores)

for c, v in enumerate(valores):
   
    print(f'Na posicao {c} encontrei o valor {v}!')

print('Cheguei ao final da lista.')

print('=' * 30)

valor = list()

for cont in range(0, 5):

    valor.append(int(input('Digite um valor: ')))

for c, v in enumerate(valor):

    print(f'Na posicao {c} achei o valor {v}!')

print('Cheguei ao fim da lista.')

print('=' * 30)

a = [1, 2, 3, 4]

b = a[:]  #? Como fazer uma copia de uma lista, sem o "[:]", ele faz uma ligacao e qualquer alteracao ira afetar as duas listas

b[2] = 8

print(f'Lista A = {a}')

print(f'Lista B = {b}')
