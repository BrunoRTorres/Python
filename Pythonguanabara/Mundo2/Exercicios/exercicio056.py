somaIdade = 0

maioridadeHomem = 0

nomeVelho = ''

totMulher20 = 0

for p in range(1, 5):

    print('==== {}ª PESSOA ===='.format(p))

    nome = str(input('Nome: ')).strip()

    idade = int(input('Idade: '))

    sexo = str(input('Sexo [M/F]: ')).strip()

    somaIdade += idade

    if p == 1 and sexo in 'Mm':

        maioridadeHomem = idade

        nomeVelho = nome

    if sexo in 'Mm' and idade > maioridadeHomem:

        maioridadeHomem = idade

        nomeVelho = nome

    if sexo in 'Ff' and idade < 20:

        totMulher20 += 1

mediaIdade = somaIdade / 4

print('A media de idade do grupo e de {} anos'.format(mediaIdade))

print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeHomem, nomeVelho.title()))

print('Ao todo sao {} mulheres com menos de 20 anos'.format(totMulher20))
