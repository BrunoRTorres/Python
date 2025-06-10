aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Media do aluno: '))

print('=-' * 15 + '=')

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'O {k} e igual a {v}.')

print('=-' * 15 + '=')
