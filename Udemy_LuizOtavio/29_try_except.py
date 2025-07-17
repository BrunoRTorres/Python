'''
Introducao ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
'''

numero_str = input('Vou dobrar o numero que voce digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} e {numero_float}')
except:
    print('Isso nao e um numero')
