valor = int(input('Digite um valor: '))

cor = {'limpa' : '\033[m', 
       'azul' : '\033[34m', 
       'verde' : '\033[32m'}

print('O numero que voce digitou e {}{}{}, {}{}{} vem antes dele e {}{}{} vem depois'.format(cor['azul'], valor, cor['limpa'], cor['verde'], valor - 1, cor['limpa'], cor['verde'], valor + 1, cor['limpa']))
