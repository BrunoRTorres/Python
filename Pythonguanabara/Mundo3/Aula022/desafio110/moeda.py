def aumentar(valor=0, taxa=0, cifrao=False):
    total = valor + (valor * taxa/100)
    return total if cifrao is False else moeda(total)      


def diminuir(valor=0, taxa=0, cifrao=False):
    total = valor - (valor * taxa/100)
    return total if cifrao is False else moeda(total) 


def dobro(valor=0, cifrao=False):
    total = valor * 2
    return total if cifrao is False else moeda(total)


def metade(valor=0, cifrao=False):
    total =  valor / 2
    return total if cifrao is False else moeda(total)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')


def resumo(valor=0, aumento=0, reducao=0):
    print('=' * 25)
    print('     RESUMO DO VALOR')
    print('=' * 25)
    print(f'Preco analisado: {moeda(valor)}')
    print(f'Dobro do preco: {dobro(valor, True)}')
    print(f'Metade do preco: {metade(valor, True)}')
    print(f'80% de aumento: {aumentar(valor, 80, True)}')
    print(f'30% de reducao: {diminuir(valor, 30, True)}')
