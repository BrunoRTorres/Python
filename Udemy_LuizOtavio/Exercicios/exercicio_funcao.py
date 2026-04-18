# Exercícios com funções

#* Crie uma função que multiplica todos os argumentos
#* não nomeados recebidos
#* Retorne o total para uma variável e mostre o valor
#* da variável

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicacao_1 = multiplicar(1, 2, 3)
print(multiplicacao_1)

print('=-=-=-=')
#* Crie uma função que fala se um número é par ou ímpar.
#* Retorne se o número é par ou ímpar.

def impar_par(x):
    if x % 2 == 0:
        return f'{x} é Par'
    return f'{x} é Impar'


numero_1 = impar_par(2)
numero_2 = impar_par(3)

print(numero_1)
print(numero_2)
