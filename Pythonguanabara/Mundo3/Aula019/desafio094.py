pessoas = list()
pessoa = dict()

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while pessoa['sexo'] not in 'MF':
        print('DADO INVALIDO! Digite M ou F!')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoakkk)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        print('DADO INVALIDO! Digite S ou N!')
        continuar = str(input('Deseja continuar? [S/N] '))
    if continuar == 'N':
        break

print(pessoas)