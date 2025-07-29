"""
    ! Lista de listas e seus indices
"""

salas = [
    # 0         1
    ['Pamela', 'Bruno'], # 0
    # 0
    ['Alice'], # 1
    # 0       1       2
    ['Luiz', 'Joao', 'Eduarda', (0, 1, 2, 3, 4)] # 2
]

print(salas)

# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala e: {sala}')
    for aluno in sala:
        print(aluno)