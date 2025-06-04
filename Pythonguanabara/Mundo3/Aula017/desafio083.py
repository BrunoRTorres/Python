expressao = str(input('Digite uma expressao matematica: '))
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append('(')
            break

if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao nao esta valida!')
