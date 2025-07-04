# Aula sobre funcoes

#! Fundamentos

#? Exemplo de funcao
'''
def mostraLinha():
    print('-------------------')


mostraLinha()
'''

#? Exemplo de funcao com parametro
'''
def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


titulo('    Curso em video  ')
'''

#@ Pratica

def soma (a, b):
    s = a + b
    print(s)


def quebraLinha():
    print('=-' * 10 + '=')


soma(4, 5)
soma(1, 9)
soma(6, 7)
soma(b=4, a=1) #? Pode inverter a ordem do parametro contanto que voce explicite os valores

quebraLinha()

def contador(*num): #? Desempacotamento dos numeros
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros.')


contador(1, 2, 3)
contador(4, 5, 6, 4, 2)
contador(1, 3)

quebraLinha()

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [4, 3, 6, 8, 1, 9]
dobra(valores)
print(valores)

quebraLinha()

def soma2(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma2(4, 1, 5)
soma2(5, 7)