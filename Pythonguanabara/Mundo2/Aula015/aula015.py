# Aula interromper while

#! Estrutura

#? while true:

#?     if teste:

#?         teste

#?     if teste:

#?         teste

#?     if teste:

#?         teste

#?         break

#? teste

#@ Pratica

n = s = 0

while True:

    n = int(input('Digite um numero: '))

    if n == 999:

        break

    s += n

print(f'A soma vale {s}')

