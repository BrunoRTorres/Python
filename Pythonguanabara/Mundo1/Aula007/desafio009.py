valor = int(input('Digite um numero: '))

cor = {'limpa' : '\033[m', 
       'verde' : '\033[32m', 
       'azul' : '\033[34m'}

print('Veja a tabuada do numero digitado \n{}{}{} x 1 = {}{}{}'.format(cor['verde'], valor, cor['limpa'], cor['azul'], valor * 1, cor['limpa']))

print('{}{}{} x 2 = {}{}{}'.format(cor['verde'], valor, cor['limpa'], cor['azul'], valor * 2, cor['limpa']))

print('{}{}{} x 3 = {}{}{}'.format(cor['verde'], valor, cor['limpa'], cor['azul'], valor * 3, cor['limpa']))

print('{}{}{} x 4 = {}{}{}'.format(cor['verde'], valor, cor['limpa'], cor['azul'], valor * 4, cor['limpa']))

print('{}{}{} x 5 = {}{}{}'.format(cor['verde'], valor, cor['limpa'], cor['azul'], valor * 5, cor['limpa']))

print('{}{}{} x 6 = {}{}{}'.format(cor['verde'], valor, cor['limpa'], cor['azul'], valor * 6, cor['limpa']))

print('{}{}{} x 7 = {}{}{}'.format(cor['verde'], valor, cor['limpa'], cor['azul'], valor * 7, cor['limpa']))

print('{}{}{} x 8 = {}{}{}'.format(cor['verde'], valor, cor['limpa'], cor['azul'], valor * 8, cor['limpa']))

print('{}{}{} x 9 = {}{}{}'.format(cor['verde'], valor, cor['limpa'], cor['azul'], valor * 9, cor['limpa']))
