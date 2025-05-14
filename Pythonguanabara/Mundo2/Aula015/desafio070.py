carrinho = produto1000 = menorPreco = cont = 0

produtoMenor = ' '

while True:

    produto = str(input('Produto: '))
    
    preco = float(input('Valor: R$'))

    cont += 1
    
    carrinho += preco

    fecha = ' '

    while fecha not in 'SN':

        fecha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if preco > 1000:

        produto1000 += 1  # conta quantos produtos custa mais de R$1000

    if cont == 1:
        
        menorPreco = preco
        
        produtoMenor = produto

    else:

        if preco < menorPreco:

            menorPreco = preco

            produtoMenor = produto

    if fecha == 'N':

        break

print(f'Seu carrinho esta em \033[32mR${carrinho:.2f}\033[m.')

print(f'Seu carrinho possui {produto1000} itens custando mais de R$1000.')

print(f'O produto mais barato {produtoMenor} custa R${menorPreco:.2f}.')
