palavras = ('jogos', 'videogame', 'computador', 'programas', 
            'software', 'casamento', 'casa', 'filhos', 'estudar',
            'trabalhar', 'programar', 'hardware', 'monitor', 'mouse',
            'teclado', 'fone de ouvido', 'televisao', 'celular', 'lapis', 
            'copo', 'capa', 'arma', 'teto')

for p in palavras:

    print(f'\nNa palavra \033[34m{p.upper()}\033[m temos as vogais: ', end='')

    for letra in p:

        if letra in 'aeiou':

            print(f'\033[32m{letra.lower()}\033[m', end= ' ')
