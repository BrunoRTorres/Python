"""
    ! Desempacotamento em chamadas de métodos e funções
"""
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0         1
    ['Pamela', 'Bruno'], # 0
    # 0
    ['Alice'], # 1
    # 0       1       2
    ['Luiz', 'Joao', 'Eduarda', (0, 1, 2, 3, 4)] # 2
]

# p, b, c, *_, ap, u = lista
# print(p, u, ap)

print(*salas, sep='\n')
