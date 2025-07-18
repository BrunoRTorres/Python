#       012345678911
nome = 'Bruno Ribas'

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

contador = 0
novo_nome = ''
while contador < len(nome):
    letra = nome[contador]
    novo_nome += letra
    novo_nome += '*'
    contador += 1

print(novo_nome)