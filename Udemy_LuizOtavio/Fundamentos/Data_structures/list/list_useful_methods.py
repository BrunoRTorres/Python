"""
    ! Listas em Python
    ? Tipo list - Mutavel
    ? Suporta varios valores de qualquer tipo
    ? Conhecimentos reutilizaveis - indices e fatiamento
    ? Metodos uteis: append, insert, pop, del, clear, extend, +
    ? Create Read Update   Delete
    ? Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, 'Removido,', ultimo_valor)
