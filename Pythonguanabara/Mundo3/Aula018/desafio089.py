alunos = []

while True:
    aluno = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([aluno, [nota1, nota2], media])
    
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar != 'S':
        break

for i, aluno in enumerate(alunos):
    print(f'{i}', aluno[0], aluno[2])

while True:
    opcao = input('Mostrar as notas de qual aluno? [999] para finalizar ')
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao == 999:
            break
        elif 0 <= opcao < len(alunos):
            print(f'Notas do aluno {alunos[opcao][0]}: {alunos[opcao][1]}')
        else:
            print('Numero invalido!')
    else:
        print('Entrada invalida! Digite um numero.')