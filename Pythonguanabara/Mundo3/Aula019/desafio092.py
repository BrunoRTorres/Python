from datetime import date

trabalhador = dict()

while True:
    trabalhador['nome'] = str(input('Nome do trabalhador: ')).capitalize()
    ano = int(input('Ano de nascimento: '))
    idade = date.today().year - ano
    trabalhador['idade'] = idade
    trabalhador['ctps'] = int(input('Carteira de trabalho [0 nao tem]: '))
    if trabalhador['ctps'] == 0:
        break
    trabalhador['contratacao'] = int(input('Ano de contratacao: '))
    trabalhador['salario'] = float(input('Salario: R$'))
    comecocareira = trabalhador['contratacao'] - ano
    trabalhador['aposentadoria'] = comecocareira + 35
    break
print('=-' * 17 + '=')

for k, v in trabalhador.items():
    print(f' - {k} tem valor {v}.')
print('=-' * 17 + '=')
