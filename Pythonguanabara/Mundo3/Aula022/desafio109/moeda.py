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
