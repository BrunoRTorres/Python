print('=-' * 8 + '=')

print('''Sexo Masculino: 1
Sexo Feminino: 2''')

media = 0

velho = ''

mulher = 0

idadeVelho = 0

for pess in range(1, 5):

    print('=-' * 8 + '=')

    nome = str(input('Qual o seu nome? '))

    idade = int(input('Quantos anos voce tem? '))

    sexo = int(input('Digite o valor do seu sexo: '))

    media += idade

    if pess == 1 and sexo == 1:

        idadeVelho = idade

        velho = nome

    if sexo == 1 and idade > idadeVelho:

        idadeVelho = idade

        velho = nome

    if sexo == 2 and idade < 20:

        mulher += 1

print('=-' * 8 + '=')

print('A media da idade das pessoas e {:.2f}'.format(media / 4))

print('O homem mais velho: {}'.format(velho).title())

print('Temos {} mulheres abaixo de 20 anos'.format(mulher))
