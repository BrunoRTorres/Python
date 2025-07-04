import moeda

valor = float(input('Digite um valor: R$'))

print(f'Com um aumento de 50%, temos {moeda.aumentar(valor, 50, True)}')
print(f'O dobro de {moeda.moeda(valor)}, temos {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.moeda(valor)}, temos {moeda.metade(valor, True)}')
