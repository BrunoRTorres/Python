# Operadores aritmeticos

#  soma  
# 5 + 2 == 7

# subtracao
# 5 - 2 == 3

# multiplicacao
# 5 * 2 == 10

# divisao 
# 5 / 2 == 2.5

# exponenciacao 
# 5 ** 2 == 25

# divisao inteira
# 5 // 2 == 2

# resto da divisao
# 5  % 2 == 1

# ordem de precedencia
# primeiro  ()
# segundo  **
# terceiro *, /, //, %  quem aparecer primeiro
# quarto + - quem aparecer primeiro

print(5 + 3 * 2)

print(3 * 5 + 4 ** 2)

print(3 * (5 + 4) ** 2)

n1 = int(input('Digite um valor: '))

n2 = int(input('Digite outro: '))

s = n1 + n2

m = n1 * n2

d = n1 / n2

di = n1 // n2

e = n1 ** n2

print('A soma e {}, \n o produto e {} e a \n divisao e {:.3f}'.format(s, m, d), end=' --- ')

print('Divisao inteira {} e potencia {}'.format(di, e))
