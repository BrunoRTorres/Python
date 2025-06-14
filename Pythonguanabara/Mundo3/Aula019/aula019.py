# Aulas sobre dicionarios

#! Fundamentos

#? Declaracao do dicionariq
# dados = dict{} 

#? Exemplo de dicionario
# dados = {'nome':'Pedro', 'idade':25}

#? Adiciona um novo elemento (append nao funciona em dicionarios)
# dados['sexo'] = 'M'

#? Revome o elemento do dicionario
# del dados['idade']

#? Outro exemplo de dicionario
# filme = {'titulo':'Star Wars',
#          'ano':1977,
#          'diretor':'George Lucas'}

#? Retorna os valores (['Star Wars', 1977, 'George Lucas])
# print(filme.values())

#? Retorna as chaves (['titulo', 'ano', 'diretor')]
# print(filme.keys())

#? Retorna os valores e chaves (['titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])
# print(filme.items())

#? Exemplo de laco
# for k, v in filme.items():
#    print(f'O {k} e {v}')

#@ Pratica

pessoas = {'nomes': 'Gustavo',
           'sexo': 'M',
           'idade': 22}

print(f'O {pessoas["nomes"]} tem {pessoas["idade"]} anos.')

print('=' * 30)

print(pessoas.items())

print('=' * 30)

for k in pessoas.keys():
    print(k)

print('=' * 30)

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('=' * 30)

pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('=' * 30)

brasil = []
estado1 = {'uf': 'Rio de Janeiro',
           'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo',
           'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['sigla'])

print('=' * 30)

estado = dict()
brazil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brazil.append(estado.copy())

for e in brazil:
    for k, v in e.items():    
        print(f'O campo {k} tem valor {v}')

print('=' * 30)
