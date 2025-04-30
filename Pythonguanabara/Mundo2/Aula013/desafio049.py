n = int(input('Digite um numero: '))

print('=-' * 10 + '=')

print('Tabuada do numero {}'.format(n))

print('=-' * 10 + '=')

s = 0

for c in range(1, 11):

    s += n

    print('{} x {} = {}'.format(n, c, s))

print('=-' * 10 + '=')