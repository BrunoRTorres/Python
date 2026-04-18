'''
    Crie funções que duplicam, triplicam e quadruplicam
    o número recebido como parâmetro.
'''

def cria_multiplicador(multiplicador):
    def operacao(numero):
        return numero * multiplicador
    return operacao


duplicador = cria_multiplicador(2)
triplicador = cria_multiplicador(3)
quadruplicador = cria_multiplicador(4)

print(duplicador(2))
print(triplicador(2))
print(quadruplicador(2))
print(triplicador(3))
