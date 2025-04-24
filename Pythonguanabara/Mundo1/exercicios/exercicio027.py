nome = str(input('Digite o seu nome: ')).strip()

nomeSplit = nome.split()

print('O seu primeiro nome: {}'.format(nomeSplit [0]))

print('O seu ultmo nome: {}'.format(nomeSplit [len(nomeSplit) -1]))
