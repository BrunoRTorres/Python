nome = str(input('Digite seu nome: ')).strip()

print(nome.upper())

print(nome.lower())

print(len(nome) - nome.count(' '))

dividido = nome.split()

print(len(dividido[0]))
