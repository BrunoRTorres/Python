# Aula condicionais

#! Estrutura da condicao

#? if teste.teste():

#?    bloco True

#? else:

#?    bloco False

#@ pratica

tempo = int(input('Quantos anos tem seu carro: '))

if tempo <= 3:

    print('Carro novo')

else:
    
    print('Carro velho')

nome = str(input('Digite o seu nome: ')).capitalize()

if nome == ('Bruno'):

    print('Que nome lindo voce tem!')

else:

    print('O seu nome e tao normal!')

print('Bom dia, {}!'.format(nome))

nota1 = float(input('Digite a primeira nota: '))

nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 6.0:

    print('Parabens, voce esta aprovado!')

else:

    print('Voce esta reprovado, estude mais!')
