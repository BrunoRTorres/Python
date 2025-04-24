# Aula de tipos primitivos e saída de dados

# int - 7, 10, -45, -1484

# float - 1.7, 1.53, -71.46, 10.0

# bool - True, False

# str - 'Oi', '7.5', 'Bruno', ''

n1 = int(input('Digite um valor: '))

n2 = int(input('Digite outro: '))

s = n1 + n2

#print('A soma entre', n1, 'e' , n2, 'vale', s)

print('A soma entre {} e {} vale {}'.format(n1, n2, s))
