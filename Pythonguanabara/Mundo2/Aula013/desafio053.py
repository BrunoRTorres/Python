frase = str(input('Digite alguma frase: ')).strip().upper()

palavras = frase.split()

junto = ''.join(palavras)

inverso = ''

for letras in range( len(junto) -1, -1, -1):

    inverso += junto[letras]

print('O inverso de {} e {}'.format(junto, inverso))

if inverso == junto:

    print('Temos um palindromo!')

else:

    print('A frase nao e um palindromo')
