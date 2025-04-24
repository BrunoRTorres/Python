valor = input('Digite algo: ')


print(type('Tipo primtivo:'))

print('O que voce digitou e um valor alpha:\033[34m',valor.isalpha(),'\033[m')

print('O que voce digitou e um numero:\033[34m',valor.isnumeric(),'\033[m')

print('O que voce digitou e alphanumerico:\033[34m',valor.isalnum(),'\033[m')

print('O que voce digitou e um espaco:\033[34m',valor.isspace(),'\033[m')
