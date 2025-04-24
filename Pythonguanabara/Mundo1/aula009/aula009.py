# Aula de manipulacao de texto

frase = '   Bruno Ribas Torres   '

#! Fatiamento

    # frase[9] = caractere 9

    # frase[9:13] = caractere 9 ate o 13, excluindo o 13 caractere

    # frase[9:18:2] = comeca no caractere 9, pulando de 2 em 2 caracteres ate o 17 caractere

    # frase[:5] = comeca no primeiro caractere ate o quarto caractere

    # frase[15:] = comeca no 15 caractere ate o final da string

    # frase[9::3] = comeca no 9 caractere ate o final, pulando de 3 em 3 caracteres

#! Analise 

    # len(frase) = mostra o comprimento da frase, contando os espacos

    # frase.count('o') = conta quantos caracteres tem na string

    # frase.count('o', 0, 13) = conta quantos caracteres tem na string dentro do alcance determinado

    # frase.find('uno') = mostra quantas vezes encontrou 'uno' dentro da string e aonde comeca

    # frase.find('silva') = retorna -1, pois nao existe na string

    # 'Bruno' in frase = retorna true, pois existe 'Bruno' na string

#! Transformacao   

    # frase.replace('Torres, Mourao') = substitui Torres por Mourao #? nao ira mudar a variavel

    # frase.upper() = modifica os caracteres minusculas em maiusculas

    # frase.lower() = modifica os caracteres maiusculas em minusculas

    # frase.capitalize() = coloca todos os caracteres em minuscula, e a primeira em maiuscula

    # frase.title() = analisa quantas palavras tem na string pelos espacos e transforma o primeiro caractere de cada palavra em maiuscula

    # frase.strip() = remove os espacos no inicio e no fim da string

    # frase.rstrip() = remove os espacos da direita da string

    # frase.lstrip() = remove os espacos da esquerda da string

#! Divisao 

    # frase.split() = separa as palavras de acordo com os espacos entre elas ['Bruno', 'Ribas', 'Torres']

#! Juncao

    # '-'.join(frase) = junta as palavras com o caractere utilizado [Bruno-Ribas-Torres]


#@ pratica

print(frase)

print(frase[9])

print(frase[::2])

print("""Bruno Ribas Torres
Pamela Agostinho Mourao
Alice Mourao Torres""")

print(frase.count('r'))

print(frase.upper().count('R'))

print(len(frase))

print(len(frase.strip()))

print(frase.replace('Torres', 'Mourao'))

print(frase.find('Bruno'))

print(frase.find('Mourao'))

dividido = frase.split()

print(frase.split())

print(dividido[0])

print(dividido[0] [1])