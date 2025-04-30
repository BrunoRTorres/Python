ano = int(input('Quantos anos voce tem? '))

servir = 18

if ano == servir:

    print('Voce precisa se alistar esse ano!')

elif ano < servir:

    falta = servir - ano

    print('Ainda nao esta na hora de se alistar, falta {} ano(s)'.format(falta))

elif ano > servir:

    atraso = ano - servir

    print('Ja passou do tempo de se alistar, voce esta {} ano(s) atrasado'.format(atraso))
