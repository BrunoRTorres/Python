"""
    
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas: #? Retorna para o while principal apos terminar o laco
        print(linha, coluna)
        coluna += 1
    linha += 1

print('Acabou')
