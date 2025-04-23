# Aula de cores no python

#! adicionar cores no terminal do python

    # \033[0;33;44m  #? 0 = estilo, 33 = cor do texto, 44m = cor do fundo

#! codigos do estilo

    # 0 = none

    # 1 = bold

    # 4 = underline

    # 7 = negative

#! codigos das cores de texto

    # 30 = preto

    # 31 = vermelho

    # 32 = verde

    # 33 = amarelo

    # 34 = azul

    # 35 = roxo

    # 36 = azul claro

    # 37 = cinza

    # 97 = branco

#! codigos das cores de fundo

    # 40 = preto

    # 41 = vermelho

    # 42 = verde

    # 43 = amarelo

    # 44 = azul

    # 45 = roxo

    # 46 = azul claro

    # 47 = cinza

    # 107 = branco

#@ pratica

print('\033[34mOla, Mundo!\033[m')

print('\033[0;31;107mOla, Mundo!\033[m')

print('\033[7;33;44mOla, Mundo!\033[m')

nome = 'Bruno'

print('Ola! Muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa' : '\033[m', 
         'azul' : '\033[34m',
         'amarelo' : '\033[33m', 
         'pretoebranco' : '\033[7;97m'}

print('Ola, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))
