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
    print('=' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('=' * 35)
    print(f'Preco analisado: \t{moeda(valor)}')
    print(f'Dobro do preco: \t{dobro(valor, True)}')
    print(f'Metade do preco: \t{metade(valor, True)}')
    print(f'80% de aumento: \t{aumentar(valor, 80, True)}')
    print(f'30% de reducao: \t{diminuir(valor, 30, True)}')
