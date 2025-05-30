# Cria uma lista vazia para armazenar os valores inseridos
lista = []

# Loop para repetir 5 vezes (para receber 5 números do usuário)
for c in range(0, 5):
    
    # Solicita ao usuário que digite um valor inteiro
    n = int(input('Digite um valor: '))
    
    # Se for o primeiro valor OU se o valor for maior que o último da lista,
    # então ele deve ser adicionado ao final (pois está em ordem)
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    
    else:
        # Senão, encontra a posição correta onde o valor deve ser inserido
        pos = 0
        while pos < len(lista):
            # Quando encontrar um valor maior ou igual, insere na posição atual
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista...')
                break  # Encerra o while após a inserção
            pos += 1  # Avança para a próxima posição na lista

# Impressão final da lista com os valores já ordenados
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
