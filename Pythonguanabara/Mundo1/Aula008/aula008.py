# aula sobre modulos

# math --- biblioteca matematica
# funcao ceil - arrendonda para cima
# funcao floor - arredonda para baixo
# funcao trunc - elimina da virgula para frente
# funcao pow - potencia
# funcao sqrt - raiz qudrada
# funcao factorial - calculo fatorial

# importa o modulo math todo
import math

# importa a funcao sqrt do modulo math
# from math import sqrt

num = int(input('Digite um numero: '))

raiz = math.sqrt(num)

print('A raiz de {} e igual a {}, arredondado para cima {}, arredondado para baixo {}'.format(num, raiz, math.ceil(raiz), math.floor(raiz)))

import random

num2 = random.randint(1, 10)
print(num2)
