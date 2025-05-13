i = int(input('Primeiro termo: '))

r = int(input('Razao: '))

d = i + (10 - 1) * r
for c in range(i, d + r, r):

    print(c, end=' ')
