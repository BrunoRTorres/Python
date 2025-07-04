import moeda

valor = float(input('Digite um valor: R$'))

print(f'Com um aumento de 50%, temos {moeda.moeda(moeda.aumentar(valor, 50))}')
print(f'O dobro de {moeda.moeda(valor)}, temos {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)}, temos {moeda.moeda(moeda.metade(valor))}')
