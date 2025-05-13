primeiro = int(input('Qual o primeiro termo? '))

razao = int(input('Qual a razao? '))

termo = primeiro

cont = 1

while cont <= 10:

    print(termo, end=' ')

    termo += razao

    cont += 1
