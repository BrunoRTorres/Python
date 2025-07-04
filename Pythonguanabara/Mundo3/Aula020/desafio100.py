from random import randint

def sorteia(lst):
    for cont in range(0, 5):
        n = randint(1, 10)
        lst.append(n)
    print(f'Os numeros sorteados foram {lst}.')


def somaPar(lst):
    soma = 0
    for num in lst:
        if num % 2 == 0:
            soma += num
    print(f'Somando os numeros pares temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
