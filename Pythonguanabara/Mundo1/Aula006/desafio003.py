n1 = int(input('Digite um valor: '))

n2 = int(input('Digite outro: '))

cores = {'limpa' : '\033[m', 
         'azul' : '\033[34m', 
         'verde' : '\033[32m'}

s = n1 + n2

print('A soma entre {}{}{} e {}{}{} gera {}{}{}'.format(cores['azul'], n1, cores['limpa'],cores['azul'], n2,cores['limpa'],cores['verde'], s, cores['limpa']))
