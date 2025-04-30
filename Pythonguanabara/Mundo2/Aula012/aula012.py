# Aula de condicoes aninhadas

#! estrutura da condicao

#?     if teste.teste():
        
#?        bloco1
    
#?    elif teste.teste():

#?        bloco2

#?    elif teste.teste():

#?        bloco3

#?    else:

#?        bloco4

#@ pratica

nome = str(input('Qual o seu nome? ')).title()

if nome == 'Bruno':

    print('Que nome bonito!')

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':

    print('Seu nome e bem popular no Brasi!')

elif nome in 'Pamela Alice':

    print('Belo nome feminino!')

else:   #? Else e opcional

    print('Seu nome e bem normal!')

print('Tenha um bom dia, {}!'.format(nome))
