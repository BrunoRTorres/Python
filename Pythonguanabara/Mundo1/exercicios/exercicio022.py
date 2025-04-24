nome = str(input('Digite seu nome: ')).strip()

print('O seu nome em maiusculas: {}'.format(nome.upper()))

print('O seu nome em minusculas: {}'.format(nome.lower()))

print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

dividido = nome.split()

print('O seu primeiro nome {}, tem {} letras'.format(dividido [0], len(dividido [0])))
