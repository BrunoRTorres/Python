pessoas = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while pessoa['sexo'] not in 'MF':
        print('DADO INVALIDO! Digite M ou F!')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        print('DADO INVALIDO! Digite S ou N!')
        continuar = str(input('Deseja continuar? [S/N] '))
    if continuar == 'N':
        break
print('=-' * 20 + '=')

print(f'Ao todo temos {len(pessoas)} pessoas.')
print('=-' * 20 + '=')

media = soma / len(pessoas)
print(f'A media da idade das pessoas e {media:5.2f}')
print('=-' * 20 + '=')

print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('=-' * 20 + '=')

print('As pessoas com idade maior que a media: ')
for p in pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} => {v};', end=' ')
        print()
print('=-' * 20 + '=')
