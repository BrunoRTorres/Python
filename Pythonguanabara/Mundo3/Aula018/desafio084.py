pessoas = list()
dados = list()
totpessoas = 0

while True:
   
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    totpessoas += 1

    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if saida == 'N':
        break

print(f'Foram cadastradas no total {totpessoas} pessoas.')
print(f'O maior peso foi')
