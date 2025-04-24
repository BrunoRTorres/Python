frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra "A" aparece quantas vezes: {}'.format(frase.count('a')))

print('A letra "A" aparece pela primeira vez: {}'.format(frase.find('a') +1))

print('A letra "A" aparece pela ultima vez: {}'.format(frase.rfind('a') +1))
