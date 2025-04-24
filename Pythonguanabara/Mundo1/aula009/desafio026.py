frase = str(input('Digite uma frase: ')).strip().lower()

print('Quantas vezes aparece a letra "a": {}'.format(frase.count('a')))

print('Em que posicao ela aparece pela primeira vez: {}'.format(frase.find('a') +1))

print('Em que posicao ela aparece pela ultima vez: {}'.format(frase.rfind('a') +1))
