"""
    ! Cuidados com dados mutaveis
    ? = - copiado o valor (imutaveis)
    ? = - aponta para o mesmo valor na memoria (mutaveis)
"""

lista_a = ['Bruno', 'Pamela', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
