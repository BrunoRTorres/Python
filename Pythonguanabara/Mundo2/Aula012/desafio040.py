nota1 = float(input('Qual a primeira nota? '))

nota2 = float(input('Qual a segunda nota? '))

media = (nota1 + nota2) / 2

if media < 5.0:

    print('REPROVADO')

elif 5.0 <= media < 7.0:

    print('RECUPERACAO')

elif media <= 7.0:

    print('APROVADO')
