# Aula de funcoes mais detalhada com docstrings, Interactive Help etc.

#! Fundamentos

#* Interactive Help

# help() #? Abre o prompt de ajuda interativa
#? Mostra manuais de comandos do Python

# print(input.__doc__)
#? Imprime o documento do comando

#*Docstrings

#? Sao manuais feitos pelo criador da funcao para auxiliar quem for utiliza-la

# Exemplo de docstring
def contador(i, f, p):
    """     #? Inicio da docstring
    => Faz uma contagem e mostra na tela.
    :para i: Inicio da contagem
    :para f: Fim da contagem
    :para P: Passo da contagem
    :return: Sem retorno
    Funcao criada por Gustavo Guanabara do canal CursoemVideo.
    """ #? Fim da docstring
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


# help(contador) #? Mostra a docstring da funcao no terminal

#* Argumentos opcionais

def somar(a=0, b=0, c=0): #? O parametro valera zero caso nao informado o argumento
    s = a + b + c
    print(f'A soma vale {s}')

# somar(3, 2, 5)
# somar(8, 4)
# somar()
# somar(b=4, a=5) #? Possivel informar argumento fora de ordem, necessário informar o endereco

#* Escopo de variáveis

def teste():
    global n #? Trata a variavel n como global, deixando de criar uma local
    n = 4 #? Sera criado como variavel local, existindo tanto a global como a local
    x = 8 #? Variavel local
    print(f'Na funcao teste, n vale {n}')
    print(f'Na funcao teste, x vale {x}')


# n = 2 #? Variavel global
# teste()
# print(f'No programa principal, n vale {n}')
# print(f'No programa principal, x vale {x}') #? A variavel 'x' nao existe no escopo global, por isso o erro

#* Retorno de resultados

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


s1 = soma(3, 2, 5)
s2 = soma(1, 7)
s3 = soma(4)

# print(f'O resultados das somas foram {s1}, {s2} e {s3}.')

#@ Pratica

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados sao {f1}, {f2} e {f3}.')

n = int(input('Digite um numero: '))
print(fatorial(n))


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    

num = int(input('Digite um numero: '))
if par(num):
    print('E par!')
else:
    print('E impar!')
