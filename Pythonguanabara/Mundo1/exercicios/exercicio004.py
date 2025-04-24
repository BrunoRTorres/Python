algo = input('Digite algo: ')

print('O tipo primitivo:', type(algo))

print('So tem espacos?', algo.isspace())

print('E um numero? ', algo.isnumeric())

print('E alfabetico?', algo.isalpha())

print('E alphanumerico?', algo.isalnum())

print('Esta em maiusculas?', algo.isupper())

print('Esta em minusculas?', algo.islower())

print('Esta capitalizada?', algo.istitle())
